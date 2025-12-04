from pathlib import Path
import json


def keys_sorted(path: Path, data: dict, fix: bool = False) -> bool:
    """
    Rule: keys must be sorted alphabetically to allow easier merging with FG
    """
    formatted = json.dumps(data, indent=2, sort_keys=True) + "\n"

    with open(path, "r", encoding="utf-8") as f:
        existing = f.read()

    if sorted(data.keys()) != list(data.keys()):
        if fix:
            with open(path, "w", encoding="utf-8") as f:
                f.write(formatted)
            print(f"🔧 {path}: keys sorted automatically")
            return True
        else:
            print(f"❌ {path}: keys are not sorted alphabetically")
            return False
    return True
