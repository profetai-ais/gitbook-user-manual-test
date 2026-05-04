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


def protect_markdown_tokens(text: str):
    placeholders = {}

    patterns = [
        r"```[\s\S]*?```",          # fenced code blocks
        r"`[^`]+`",                 # inline code
        r"!\[[^\]]*\]\([^)]+\)",    # images
        r"\[[^\]]+\]\([^)]+\)",     # markdown links
        r"<[^>]+>",                 # html tags
    ]

    protected = text
    index = 0

    for pattern in patterns:
        matches = list(re.finditer(pattern, protected))
        for match in matches:
            original = match.group(0)
            token = f"ZXQPLACEHOLDER{index}QXZ"
            placeholders[token] = original
            protected = protected.replace(original, token, 1)
            index += 1

    return protected, placeholders


def restore_markdown_tokens(text: str, placeholders: dict):
    restored = text

    for token, original in placeholders.items():
        restored = restored.replace(token, original)
        restored = restored.replace(token.lower(), original)

    return restored


def split_text(text: str, max_len: int = 3000):
    chunks = []
    current = ""

    for paragraph in text.split("\n\n"):
        paragraph = paragraph.strip("\n")

        if not paragraph.strip():
            continue

        if len(current) + len(paragraph) + 2 > max_len:
            if current.strip():
                chunks.append(current)
            current = paragraph
        else:
            current += ("\n\n" if current else "") + paragraph

    if current.strip():
        chunks.append(current)

    return chunks


def translate_text(text: str):
    if not text or not text.strip():
        return text

    protected, placeholders = protect_markdown_tokens(text)
    translated_chunks = []

    for chunk in split_text(protected):
        if not chunk.strip():
            translated_chunks.append(chunk)
            continue

        try:
            translated = translator.translate(chunk)

            if translated is None:
                print("Translation returned None, keeping original chunk.")
                translated = chunk

            translated_chunks.append(str(translated))
            time.sleep(0.6)

        except Exception as exc:
            print(f"Translation failed, keeping original text. Error: {exc}")
            translated_chunks.append(str(chunk))
            time.sleep(0.6)

    translated_text = "\n\n".join(
        str(chunk) for chunk in translated_chunks if chunk is not None
    )

    return restore_markdown_tokens(translated_text, placeholders)


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

        buffer.append(line)

    flush_buffer()

    return "\n".join(str(line) for line in result if line is not None) + "\n"


def should_skip(path: Path):
    parts = set(path.parts)
    return bool(parts & EXCLUDE_DIRS)


def main():
    OUT_DIR.mkdir(exist_ok=True)

    gitbook_dir = ROOT / ".gitbook"
    if gitbook_dir.exists():
        target_gitbook_dir = OUT_DIR / ".gitbook"
        if target_gitbook_dir.exists():
            shutil.rmtree(target_gitbook_dir)
        shutil.copytree(gitbook_dir, target_gitbook_dir)

    markdown_files = [
        path for path in ROOT.rglob("*.md")
        if not should_skip(path)
    ]

    for source_path in markdown_files:
        relative_path = source_path.relative_to(ROOT)
        target_path = OUT_DIR / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"Translating {source_path} -> {target_path}")

        content = source_path.read_text(encoding="utf-8")
        translated = translate_markdown(content)
        target_path.write_text(translated, encoding="utf-8")

    print("Done.")


if __name__ == "__main__":
    main()
