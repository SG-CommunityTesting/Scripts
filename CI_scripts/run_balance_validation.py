import sys
from pathlib import Path
import json
from balance_validators import VALIDATORS

LOG_FILE = "validation_output.log"


def find_json_files(root_path: Path):
    return root_path.rglob("*.json")


def validate_file(path: Path, fix: bool = False):
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Invalid JSON ({e})"]

    failures = []

    for validator in VALIDATORS:
        if not validator(path, data, fix):
            failures.append(validator.__name__)

    return failures


def print_failure_table(failure_dict, log_path: Path = None):
    lines = []

    if not failure_dict:
        lines.append("\n🎉 All files passed validation!")
    else:
        lines.append("\n❌ Validation failures:")
        lines.append("=" * 50)
        lines.append(f"{'File':<40} Failed Rules")
        lines.append("-" * 50)
        for path, rules in failure_dict.items():
            rules_str = ", ".join(rules)
            lines.append(f"{str(path):<40} {rules_str}")
        lines.append("=" * 50)
        lines.append(f"Total failed files: {len(failure_dict)}")

    # Print to console
    print("\n".join(lines))

    # Write to log file if provided
    if log_path:
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


if __name__ == "__main__":
    args = sys.argv[1:]
    fix = "--fix" in args

    # Get --path argument
    if "--path" in args:
        idx = args.index("--path")
        root = Path(args[idx + 1])
    else:
        root = Path(".")

    failure_dict = {}

    for json_file in find_json_files(root):
        _
