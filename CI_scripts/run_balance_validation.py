import sys
from pathlib import Path
import json
from balance_validators import VALIDATORS


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


def print_failure_table(failure_dict):
    if not failure_dict:
        print("\n🎉 All files passed validation!")
        return

    print("\n❌ Validation failures:")
    print("=" * 50)
    print(f"{'File':<40} Failed Rules")
    print("-" * 50)
    for path, rules in failure_dict.items():
        rules_str = ", ".join(rules)
        print(f"{str(path):<40} {rules_str}")
    print("=" * 50)
    print(f"Total failed files: {len(failure_dict)}")


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
        failures = validate_file(json_file, fix)
        if failures:
            failure_dict[json_file] = failures

    print_failure_table(failure_dict)

    if failure_dict:
        sys.exit(1)
