from pathlib import Path
import json


def indentation_correct(path: Path, data: dict, fix: bool = False) -> bool:
    """
    Rule: File must be 2-space indented
    """
    formatted = json.dumps(data, indent=2, sort_keys=True) + "\n"

    with open(path, "r", encoding="utf-8") as f:
        existing = f.read()

    if existing != formatted:
        if fix:
            with open(path, "w", encoding="utf-8") as f:
                f.write(formatted)
            print(f"🔧 {path}: indentation corrected")
            return True
        else:
            print(f"❌ {path}: indentation is incorrect")
            return False
    return True
