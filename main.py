"""Write the original Dad Joke Showdown entry without a trailing newline."""

from pathlib import Path

JOKE = "Why did Dad replace the curtains? He finally decided to draw the line."
assert 1 <= len(JOKE) <= 200
assert "\n" not in JOKE

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(JOKE, encoding="utf-8")
# Verification: 70 characters, one joke, no trailing newline.
