from pathlib import Path
import re
import shutil
import time

from deep_translator import GoogleTranslator


ROOT = Path(".")
OUT_DIR = ROOT / "en"

EXCLUDE_DIRS = {
    ".git",
    ".github",
    "en",
    "scripts",
}

translator = GoogleTranslator(source="zh-TW", target="en")


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def split_frontmatter(content: str):
    match = re.match(r"\A(---\s*\n[\s\S]*?\n---\s*\n)([\s\S]*)\Z", content)

    if not match:
        return "", content

    return match.group(1), match.group(2)


def cleanup_orphan_placeholders(text: str):
    if not text:
        return text

    cleaned = text

    patterns = [
        r"⟬\s*PH\s*\d(?:\s*\d)*\s*⟭",
        r"⟦\s*PH\s*\d(?:\s*\d)*\s*⟧",
        r"\[\[\s*(?:PH\s*)?\d(?:\s*\d)*\s*\]\]",
        r"\[\s*(?:PH\s*)?\d(?:\s*\d)*\s*\]",
        r"\(\s*(?:PH\s*)?\d(?:\s*\d)*\s*\)",
        r"ZXQPLACEHOLDER\d+QXZ",
    ]

    for pattern in patterns:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)

    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)

    return cleaned


def protect_inline_tokens(text: str):
    placeholders = {}
    protected = text
    index = 0

    def make_token(original: str) -> str:
        nonlocal index
        token = f"QQQPROTECT{index}QQQ"
        placeholders[token] = original
        index += 1
        return token

    patterns = [
        r"`[^`]+`",
        r"\[[^\]]+\]\([^)]+\)",
    ]

    for pattern in patterns:
        matches = list(re.finditer(pattern, protected))
        for match in matches:
            original = match.group(0)
            protected = protected.replace(original, make_token(original), 1)

    return protected, placeholders


def restore_inline_tokens(text: str, placeholders: dict):
    restored = text

    for token, original in placeholders.items():
        restored = restored.replace(token, original)

        token_number = re.search(r"QQQPROTECT(\d+)QQQ", token)
        if token_number:
            number = token_number.group(1)
            restored = re.sub(
                rf"Q+\s*PROTECT\s*{number}\s*Q+",
                original,
                restored,
                flags=re.IGNORECASE,
            )

    return cleanup_orphan_placeholders(restored)


def split_long_text(text: str, max_len: int = 2200):
    if len(text) <= max_len:
        return [text]

    chunks = []
    current = ""

    for sentence in re.split(r"(?<=[。！？.!?])\s*", text):
        if not sentence:
            continue

        if len(current) + len(sentence) > max_len:
            if current.strip():
                chunks.append(current)
            current = sentence
        else:
            current += sentence

    if current.strip():
        chunks.append(current)

    return chunks or [text]


def translate_text(text: str):
    if not text or not text.strip():
        return text

    if not has_cjk(text):
        return cleanup_orphan_placeholders(text)

    protected, placeholders = protect_inline_tokens(text)
    translated_chunks = []

    for chunk in split_long_text(protected):
        try:
            translated = translator.translate(chunk)

            if translated is None:
                print("Translation returned None, keeping original text.", flush=True)
                translated = chunk

            translated_chunks.append(str(translated))
            time.sleep(0.35)

        except Exception as exc:
            print(f"Translation failed, keeping original text. Error: {exc}", flush=True)
            translated_chunks.append(str(chunk))
            time.sleep(0.35)

    translated_text = " ".join(
        str(chunk) for chunk in translated_chunks if chunk is not None
    )

    return restore_inline_tokens(translated_text, placeholders)


def is_markdown_image(line: str):
    return bool(re.search(r"!\[[^\]]*\]\([^)]+\)", line))


def is_table_line(line: str):
    return "|" in line


def starts_html_block(line: str):
    stripped = line.strip().lower()

    html_starts = [
        "<table",
        "<thead",
        "<tbody",
        "<tr",
        "<td",
        "<th",
        "<figure",
        "<img",
        "<picture",
        "<video",
        "<iframe",
        "<div",
        "<details",
        "<summary",
    ]

    return any(stripped.startswith(tag) for tag in html_starts)


def ends_html_block(line: str):
    stripped = line.strip().lower()

    html_ends = [
        "</table>",
        "</thead>",
        "</tbody>",
        "</tr>",
        "</td>",
        "</th>",
        "</figure>",
        "</picture>",
        "</video>",
        "</iframe>",
        "</div>",
        "</details>",
        "</summary>",
    ]

    return any(tag in stripped for tag in html_ends)


def translate_line(line: str):
    patterns = [
        r"^(\s{0,3}#{1,6}\s+)(.+)$",
        r"^(\s*[-*+]\s+\[[ xX]\]\s+)(.+)$",
        r"^(\s*[-*+]\s+)(.+)$",
        r"^(\s*\d+\.\s+)(.+)$",
    ]

    for pattern in patterns:
        match = re.match(pattern, line)
        if match:
            return match.group(1) + str(translate_text(match.group(2)))

    return translate_text(line)


def translate_markdown(content: str):
    frontmatter, body = split_frontmatter(content)

    lines = body.splitlines()
    result = []
    buffer = []
    in_code_block = False
    in_html_block = False

    def flush_buffer():
        if buffer:
            joined = "\n".join(buffer)
            translated = translate_text(joined)

            if translated is None:
                translated = joined

            result.append(str(translated))
            buffer.clear()

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_buffer()
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        if in_html_block:
            result.append(line)
            if ends_html_block(line):
                in_html_block = False
            continue

        if starts_html_block(line):
            flush_buffer()
            result.append(line)

            if not ends_html_block(line) and not stripped.lower().endswith("/>"):
                in_html_block = True

            continue

        if stripped == "":
            flush_buffer()
            result.append(line)
            continue

        # Safety first:
        # Keep tables and images unchanged so GitBook layout will not break.
        if is_table_line(line) or is_markdown_image(line):
            flush_buffer()
            result.append(line)
            continue

        if re.match(r"^\s{0,3}#{1,6}\s+", line):
            flush_buffer()
            result.append(translate_line(line))
            continue

        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush_buffer()
            result.append(translate_line(line))
            continue

        buffer.append(line)

    flush_buffer()

    translated_body = "\n".join(str(line) for line in result if line is not None)
    translated_body = cleanup_orphan_placeholders(translated_body)

    if translated_body:
        translated_body += "\n"

    return frontmatter + translated_body


def should_skip(path: Path):
    parts = set(path.parts)
    return bool(parts & EXCLUDE_DIRS)


def main():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)

    OUT_DIR.mkdir(exist_ok=True)

    gitbook_dir = ROOT / ".gitbook"
    if gitbook_dir.exists():
        shutil.copytree(gitbook_dir, OUT_DIR / ".gitbook")

    markdown_files = [
        path for path in ROOT.rglob("*.md")
        if not should_skip(path)
    ]

    for source_path in markdown_files:
        relative_path = source_path.relative_to(ROOT)
        target_path = OUT_DIR / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"Translating {source_path} -> {target_path}", flush=True)

        content = source_path.read_text(encoding="utf-8")
        translated = translate_markdown(content)
        target_path.write_text(translated, encoding="utf-8")

    print("Done.", flush=True)


if __name__ == "__main__":
    main()
