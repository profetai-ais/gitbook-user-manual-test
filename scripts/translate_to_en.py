from pathlib import Path
import re
import shutil
import time
import html

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


def yaml_quote(text: str) -> str:
    text = str(text).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def cleanup_orphan_placeholders(text: str):
    if not text:
        return text

    cleaned = text

    patterns = [
        r"⟬\s*PH\s*\d(?:\s*\d)*\s*⟭",
        r"⟦\s*PH\s*\d(?:\s*\d)*\s*⟧",
        r"\[\[\s*(?:PH\s*)?\d(?:\s*\d)*\s*\]\]",
        r"\[\s*PH\s*\d(?:\s*\d)*\s*\]",
        r"\(\s*PH\s*\d(?:\s*\d)*\s*\)",
        r"ZXQPLACEHOLDER\d+QXZ",
        r"Q+\s*PROTECT\s*\d+\s*Q+",
        r"T+\s*KEEP\s*\d+\s*T+",
    ]

    for pattern in patterns:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)

    cleaned = re.sub(r"(?:\[\d+\]){2,}", "", cleaned)
    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)

    return cleaned


def split_long_text(text: str, max_len: int = 1800):
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


def raw_translate(text: str):
    if not text or not text.strip():
        return text

    if not has_cjk(text):
        return cleanup_orphan_placeholders(text)

    translated_chunks = []

    for chunk in split_long_text(text):
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

    return cleanup_orphan_placeholders(
        " ".join(str(chunk) for chunk in translated_chunks if chunk is not None)
    )


def split_frontmatter(content: str):
    match = re.match(r"\A(---\s*\n[\s\S]*?\n---\s*\n)([\s\S]*)\Z", content)

    if not match:
        return "", content

    return match.group(1), match.group(2)


def translate_frontmatter(frontmatter: str):
    if not frontmatter:
        return ""

    lines = frontmatter.splitlines()

    if len(lines) < 2 or lines[0].strip() != "---":
        return frontmatter

    inner = lines[1:-1]
    output = []
    index = 0

    while index < len(inner):
        line = inner[index]

        block_match = re.match(r"^(\s*)(title|description):\s*([>|][+-]?)\s*$", line)

        if block_match:
            indent = block_match.group(1)
            key = block_match.group(2)

            block_lines = []
            index += 1

            while index < len(inner):
                next_line = inner[index]

                if re.match(r"^\S[^:]*:\s*", next_line):
                    break

                block_lines.append(next_line.strip())
                index += 1

            original_text = " ".join(part for part in block_lines if part)

            if has_cjk(original_text):
                translated_text = raw_translate(original_text)
                output.append(f"{indent}{key}: {yaml_quote(translated_text)}")
            else:
                output.append(line)
                output.extend(block_lines)

            continue

        single_match = re.match(r"^(\s*)(title|description):\s*(.*)$", line)

        if single_match:
            indent = single_match.group(1)
            key = single_match.group(2)
            value = single_match.group(3).strip()
            clean_value = value.strip("'\"")

            if has_cjk(clean_value):
                translated_value = raw_translate(clean_value)
                output.append(f"{indent}{key}: {yaml_quote(translated_value)}")
            else:
                output.append(line)

            index += 1
            continue

        output.append(line)
        index += 1

    return "---\n" + "\n".join(output) + "\n---\n"


def make_token_factory():
    placeholders = {}
    counter = {"value": 0}

    def make_token(original: str) -> str:
        number = counter["value"]
        counter["value"] += 1

        token = f"TTTKEEP{number:04d}TTT"
        placeholders[token] = original

        return token

    return make_token, placeholders


def restore_tokens(text: str, placeholders: dict):
    restored = text

    for token, original in placeholders.items():
        restored = restored.replace(token, original)

        token_match = re.search(r"TTTKEEP(\d+)", token)
        if not token_match:
            continue

        number = str(int(token_match.group(1)))
        loose_number = r"0*\s*" + r"\s*".join(re.escape(char) for char in number)

        tolerant_patterns = [
            rf"T+\s*KEEP\s*{loose_number}\s*T+",
            rf"\[\[\s*T+\s*KEEP\s*{loose_number}\s*T+\s*\]\]",
            rf"\[\s*T+\s*KEEP\s*{loose_number}\s*T+\s*\]",
            rf"\(\s*T+\s*KEEP\s*{loose_number}\s*T+\s*\)",
        ]

        for pattern in tolerant_patterns:
            restored = re.sub(pattern, original, restored, flags=re.IGNORECASE)

    return cleanup_orphan_placeholders(restored)


def protect_inline_tokens(text: str):
    make_token, placeholders = make_token_factory()
    protected = text

    protected = re.sub(
        r"!\[[^\]]*\]\([^)]+\)",
        lambda match: make_token(match.group(0)),
        protected,
    )

    protected = re.sub(
        r"`[^`]+`",
        lambda match: make_token(match.group(0)),
        protected,
    )

    def replace_link(match):
        label = match.group(1)
        url = match.group(2)

        if has_cjk(label):
            translated_label = raw_translate(label)
        else:
            translated_label = label

        return make_token(f"[{translated_label}]({url})")

    protected = re.sub(
        r"(?<!!)\[([^\]]+)\]\(([^)]+)\)",
        replace_link,
        protected,
    )

    return protected, placeholders


def translate_text(text: str):
    if not text or not text.strip():
        return text

    if not has_cjk(text):
        return cleanup_orphan_placeholders(text)

    protected, placeholders = protect_inline_tokens(text)
    translated = raw_translate(protected)

    return restore_tokens(translated, placeholders)


def translate_summary(content: str):
    frontmatter, body = split_frontmatter(content)
    translated_frontmatter = translate_frontmatter(frontmatter)

    result = []

    for line in body.splitlines():
        link_match = re.match(r"^(\s*[-*+]\s*)\[([^\]]*)\]\(([^)]+)\)(.*)$", line)

        if link_match:
            prefix = link_match.group(1)
            label = link_match.group(2)
            url = link_match.group(3)
            suffix = link_match.group(4)

            if has_cjk(label):
                translated_label = raw_translate(label)
            else:
                translated_label = cleanup_orphan_placeholders(label)

            if not translated_label.strip():
                translated_label = label

            result.append(f"{prefix}[{translated_label}]({url}){suffix}")
            continue

        heading_match = re.match(r"^(\s{0,3}#{1,6}\s+)(.+)$", line)

        if heading_match:
            prefix = heading_match.group(1)
            title = heading_match.group(2)
            translated_title = raw_translate(title) if has_cjk(title) else title
            result.append(prefix + translated_title)
            continue

        if has_cjk(line):
            result.append(raw_translate(line))
        else:
            result.append(cleanup_orphan_placeholders(line))

    translated_body = "\n".join(result)

    if translated_body:
        translated_body += "\n"

    return translated_frontmatter + translated_body


def is_symbol_only_cell(text: str):
    stripped = cleanup_orphan_placeholders(text.strip())

    if not stripped:
        return True

    symbol_values = {
        "O",
        "X",
        "o",
        "x",
        "✓",
        "✔",
        "✕",
        "✖",
        "-",
        "—",
        "–",
        "N/A",
        "n/a",
    }

    if stripped in symbol_values:
        return True

    if re.fullmatch(r"[OXox✓✔✕✖\-—–\s/]+", stripped):
        return True

    return False


def is_table_separator(line: str):
    stripped = line.strip()

    if "|" not in stripped:
        return False

    cells = [cell.strip() for cell in stripped.strip("|").split("|")]

    if not cells:
        return False

    return all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def is_markdown_table_line(line: str):
    return "|" in line


def translate_markdown_table_line(line: str):
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

        if re.search(r"!\[[^\]]*\]\([^)]+\)", core):
            translated_core = core
        elif is_symbol_only_cell(core):
            translated_core = cleanup_orphan_placeholders(core)
        else:
            translated_core = translate_text(core)

        translated_parts.append(
            (" " * leading) + str(translated_core) + (" " * trailing)
        )

    return "|".join(translated_parts)


def translate_html_text_nodes(line: str):
    """
    Translate text between HTML tags while preserving tags and attributes.

    Example:
    <td>管理 Agent</td>
    -> <td>Manage Agent</td>
    """
    if not has_cjk(line):
        return cleanup_orphan_placeholders(line)

    # Keep image-like lines unchanged.
    if re.search(r"<\s*(img|video|iframe|source|picture)\b", line, flags=re.IGNORECASE):
        return line

    parts = re.split(r"(<[^>]+>)", line)
    output = []

    for part in parts:
        if not part:
            continue

        if part.startswith("<") and part.endswith(">"):
            output.append(part)
            continue

        if has_cjk(part):
            leading = re.match(r"^\s*", part).group(0)
            trailing = re.search(r"\s*$", part).group(0)
            core = part.strip()

            if is_symbol_only_cell(core):
                translated_core = cleanup_orphan_placeholders(core)
            else:
                translated_core = translate_text(html.unescape(core))

            output.append(leading + str(translated_core) + trailing)
        else:
            output.append(cleanup_orphan_placeholders(part))

    return "".join(output)


def is_markdown_image(line: str):
    return bool(re.search(r"!\[[^\]]*\]\([^)]+\)", line))


def is_gitbook_directive(line: str):
    stripped = line.strip()

    return stripped.startswith("{%") or stripped.endswith("%}")


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
    translated_frontmatter = translate_frontmatter(frontmatter)

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
            result.append(translate_html_text_nodes(line))
            if ends_html_block(line):
                in_html_block = False
            continue

        if starts_html_block(line):
            flush_buffer()
            result.append(translate_html_text_nodes(line))

            if not ends_html_block(line) and not stripped.lower().endswith("/>"):
                in_html_block = True

            continue

        if is_gitbook_directive(line):
            flush_buffer()
            result.append(line)
            continue

        if stripped == "":
            flush_buffer()
            result.append(line)
            continue

        if is_markdown_image(line):
            flush_buffer()
            result.append(line)
            continue

        if is_markdown_table_line(line):
            flush_buffer()
            result.append(translate_markdown_table_line(line))
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

    return translated_frontmatter + translated_body


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

        if source_path.name == "SUMMARY.md":
            translated = translate_summary(content)
        else:
            translated = translate_markdown(content)

        target_path.write_text(translated, encoding="utf-8")

    print("Done.", flush=True)


if __name__ == "__main__":
    main()
