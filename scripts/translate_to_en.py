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


def protect_markdown_tokens(text: str):
    placeholders = {}
    protected = text
    index = 0

    def make_token(original: str) -> str:
        nonlocal index
        token = f"⟦{index}⟧"
        placeholders[token] = original
        index += 1
        return token

    patterns = [
        r"!\[[^\]]*\]\([^)]+\)",    # images
        r"`[^`]+`",                 # inline code
        r"<[^>]+>",                 # html tags
    ]

    for pattern in patterns:
        matches = list(re.finditer(pattern, protected))
        for match in matches:
            original = match.group(0)
            protected = protected.replace(original, make_token(original), 1)

    # Protect URLs inside normal markdown links, but allow link text to translate.
    def protect_link_url(match):
        label = match.group(1)
        url = match.group(2)
        return f"{label}({make_token(url)})"

    protected = re.sub(r"(\[[^\]]+\])\(([^)]+)\)", protect_link_url, protected)

    return protected, placeholders


def restore_markdown_tokens(text: str, placeholders: dict):
    restored = text

    for token, original in placeholders.items():
        restored = restored.replace(token, original)

    return restored


def translate_text(text: str):
    if not text or not text.strip():
        return text

    if not has_cjk(text):
        return text

    protected, placeholders = protect_markdown_tokens(text)

    try:
        translated = translator.translate(protected)

        if translated is None:
            print("Translation returned None, keeping original text.", flush=True)
            translated = protected

        time.sleep(0.35)
        return restore_markdown_tokens(str(translated), placeholders)

    except Exception as exc:
        print(f"Translation failed, keeping original text. Error: {exc}", flush=True)
        return restore_markdown_tokens(protected, placeholders)


def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped:
        return False

    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if not cells:
        return False

    return all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def translate_table_line(line: str):
    if is_table_separator(line):
        return line

    parts = line.split("|")
    translated_parts = []

    for part in parts:
        if not part.strip():
            translated_parts.append(part)
            continue

        leading = len(part) - len(part.lstrip())
        trailing = len(part) - len(part.rstrip())
        core = part.strip()

        translated_core = translate_text(core)

        translated_parts.append(
            (" " * leading) + translated_core + (" " * trailing)
        )

    return "|".join(translated_parts)


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
            return match.group(1) + translate_text(match.group(2))

    return translate_text(line)


def translate_markdown(content: str):
    lines = content.splitlines()
    result = []
    buffer = []
    in_code_block = False

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

        if stripped == "":
            flush_buffer()
            result.append(line)
            continue

        if "|" in line:
            flush_buffer()
            result.append(translate_table_line(line))
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

    return "\n".join(str(line) for line in result if line is not None) + "\n"


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
