#!/usr/bin/env python3
"""Check the public strategy-card contract with the standard library only."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "## Strategy",
    "## Audience and context",
    "## Teaching problem",
    "## Facilitator move",
    "## Learner evidence",
    "## Feedback and adaptation",
    "## Accessibility",
    "## Responsible-use boundary",
    "## Verification",
    "## What this does and does not prove",
)
APPROVED_EXTERNAL = (
    "https://github.com/julie-elkins/",
    "https://www.youtube.com/",
)


def main() -> int:
    cards = sorted((ROOT / "strategies").glob("*.md"))
    errors: list[str] = []
    if not cards:
        errors.append("no strategy cards found")

    for card in cards:
        text = card.read_text(encoding="utf-8")
        for heading in REQUIRED:
            if heading not in text:
                errors.append(f"{card.name}: missing {heading}")
        for url in re.findall(r"https?://[^\s)>]+", text):
            if not url.startswith(APPROVED_EXTERNAL):
                errors.append(f"{card.name}: unapproved external URL {url}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"checked {len(cards)} strategy cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
