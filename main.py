"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Deterministic: no randomness, no time, no network, stdlib only.
"""

import os

JOKE = (
    "I asked my daughter why her shoes were in the freezer. "
    "'To keep them cool,' she said. "
    "'Well, at least they're not running.'"
)


def main():
    # The bounty requires 1-200 characters; fail loudly instead of
    # writing an entry that cannot score.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
