#!/usr/bin/env python3
"""Apply the two supplied Simplified Chinese status translations, failing on upstream drift."""
from pathlib import Path
import sys

SOURCE = Path("FloatingButtonWindow.m")
TRANSLATIONS = {
    'subtitle = @"Immortalized";': 'subtitle = @"已开启真后台";',
    'subtitle = @"At Rest";': 'subtitle = @"正常模式";',
}

def main():
    source = SOURCE.read_text(encoding="utf-8")
    for original, translated in TRANSLATIONS.items():
        old_count, new_count = source.count(original), source.count(translated)
        if (old_count, new_count) == (1, 0):
            source = source.replace(original, translated)
        elif (old_count, new_count) == (0, 1):
            pass  # Already localized in this fork.
        else:
            sys.exit(f"Localization stopped: unexpected upstream string: {original} ({old_count}/{new_count})")
    SOURCE.write_text(source, encoding="utf-8")
    print("Both v3 status labels are localized.")

if __name__ == "__main__":
    main()
