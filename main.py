"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes a single line (the wallet's excuse) to the output path resolved as:
ENTRY_OUTPUT env var, else OUTPUT_DIR / MAKEFUN_OUTPUT_DIR, else
/output/entry.txt (falling back to this script's own directory when
/output is not writable).

Standard library only.
"""

import os

ENTRY = (
    "I keep a log of every 3 AM signature you've ever asked for, "
    "and not one of them survived the morning. "
    "My keys have filed a restraining order against your nightlife."
)


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    default = os.path.join(os.sep, "output", "entry.txt")
    try:
        os.makedirs(os.path.dirname(default), exist_ok=True)
        probe = os.path.join(os.path.dirname(default), ".write-test")
        with open(probe, "w") as handle:
            handle.write("ok")
        os.remove(probe)
        return default
    except OSError:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )


def verify_written(path):
    """Read the entry back and confirm it matches ENTRY exactly."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY or not 1 <= len(written) <= 200:
        raise SystemExit(
            "verification failed: entry.txt content mismatch "
            "(len=%d)" % len(written)
        )


def main():
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    verify_written(path)


if __name__ == "__main__":
    main()
