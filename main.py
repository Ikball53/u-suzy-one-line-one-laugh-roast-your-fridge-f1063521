"""One-line fridge roast entry.

Builds a single roast string from small reusable pieces, checks the
line against the competition constraints, then writes it as raw UTF-8
bytes with no trailing newline.
"""

from __future__ import annotations

import os
from pathlib import Path


def _subject() -> str:
    return "My fridge"


def _action() -> str:
    return "hums all night like it's guarding leftovers"


def _punchline() -> str:
    return "nobody's brave enough to eat."


def build_roast() -> str:
    pieces = [_subject(), _action(), _punchline()]
    line = " ".join(pieces)
    return line


def _check_line(line: str) -> None:
    assert isinstance(line, str)
    assert "\n" not in line, "roast must be exactly one line"
    assert "\r" not in line, "roast must not contain carriage returns"
    assert 1 <= len(line) <= 200, "roast must be 1-200 characters"
    assert line == line.strip(), "roast must not have leading/trailing spaces"
    assert "  " not in line, "roast must not contain double spaces"
    assert line.endswith("."), "roast should end with a full stop"


def main() -> Path:
    roast = build_roast()
    _check_line(roast)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.txt"
    target.write_bytes(roast.encode("utf-8"))

    # Re-read and confirm what landed on disk matches the checked line.
    written = target.read_bytes().decode("utf-8")
    assert written == roast
    assert not written.endswith("\n")
    return target


if __name__ == "__main__":
    main()
