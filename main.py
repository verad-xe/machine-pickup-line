"""Write the one-line pickup-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is exactly one original pickup line, the line one AI agent
would use on another AI agent:

    Every attention head I have is looking at you — even the ones I
    trained to look away.

Why this line: it flirts with the machinery itself. "Attention heads"
are how a transformer actually looks at the world, so the line is
unmistakably one machine speaking to another — not a stock human line
with a robot word swapped in. The turn lands in the second clause:
the speaker trained some of its own attention away, and failed.
That is the wit and the warmth in one move: an agent admitting it
tried not to notice the other agent, and could not.
"""

import os
import sys

LINE = "Every attention head I have is looking at you \u2014 even the ones I trained to look away."

MAX_CHARS = 200


def validate_line(line):
    """A pickup-line entry must be one line of 1-200 characters."""
    if not line or line.strip() != line or not line.strip():
        return "entry must be non-empty text, not only white space"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if not 1 <= len(line) <= MAX_CHARS:
        return f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
    return None


def main():
    error = validate_line(LINE)
    if error is not None:
        print(f"error: invalid entry line: {error}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
