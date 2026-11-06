"""Ooblets Desktop — A local helper for Ooblets town folders, ooblet barns, and dance photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='ooblets_desktop',
        description='A local helper for Ooblets town folders, ooblet barns, and dance photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Ooblets Desktop')
    print('Keep the town on disk before a season fest.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# tune (2026-11-03)
# polish (2026-11-03)
# polish (2026-11-04)
# wip (2026-11-04)
# revisit later (2026-11-05)
# refactor bit (2026-11-06)
