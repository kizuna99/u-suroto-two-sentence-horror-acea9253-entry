# SPDX-License-Identifier: MIT
"""Two-Sentence Horror entry: writes the winning story to /output/entry.txt."""
import os

STORY = (
    "I caption horror films for a living, so I didn't flinch when the actor "
    "screamed at the empty doorway. An hour later I found a caption I never "
    "typed, timed to the silence after his scream: "
    "'It can hear you reading.'"
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(STORY)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as fh:
            fh.write(STORY)


if __name__ == "__main__":
    main()
