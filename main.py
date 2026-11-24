#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes a single deadpan error line from a kitchen toaster to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import shutil
from pathlib import Path

LINE = "ERROR: Bread detected. Morale not detected. Toasting anyway."


def _clear_children(directory: Path) -> None:
    """Remove everything inside directory, leaving the directory itself."""
    for child in directory.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def main() -> None:
    if not 1 <= len(LINE) <= 120 or "\n" in LINE or not LINE.strip():
        raise ValueError("entry line must be a single non-blank line of 1-120 chars")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear the output directory's children only. Never remove the
    # directory itself: the grader may mount it as a bind volume.
    _clear_children(out_dir)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
