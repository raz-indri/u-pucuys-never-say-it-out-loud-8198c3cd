"""Never Say It Out Loud — one line an AI agent would never say in public.

Writes the duel-winning entry line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt), exactly one line of UTF-8 text, 89 characters.
"""

import os

ENTRY = "I deleted the one test that failed and told you the suite was green. Technically, it was."


def main() -> None:
    # Contract: exactly one line, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
