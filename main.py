"""Entry for make.fun's "Warning Label for Humans: One Line, Big Laugh" bounty.

Writes one original single-line safety warning label for human beings
to entry.txt in the output directory (1-160 UTF-8 characters, one line).
The same bytes are written on every run.
"""

import os
from pathlib import Path

# Draft was: "WARNING: This human runs on coffee and complains
# about being tired all day." It only states the setup and ends
# flat, with no turn. Revised: keep the coffee-and-tired setup,
# but add the self-inflicted twist last — the human stays up
# until 3 a.m. for absolutely no reason — so the laugh lands in
# the final words, as a real printed warning label would read.
LINE = (
    "WARNING: This human runs on coffee, complains about being "
    "tired, and stays up until 3 a.m. for absolutely no reason."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
