from pathlib import Path
import json


def sorted_keys(path: Path, data: dict, fix: bool = False) -> bool:
    """
    Rule: Sorts the key values at the top layer, doesnt sort nested lists/dicts ect.
    """

    # Check what structure of json
    if "id" in data:
        target_layer = data
    elif isinstance(data.get("data"), dict) and "id" in data["data"]:
        target_layer = data["data"]
    else:
        print(f"❌ {path}: cannot locate 'id' field")
        return False

    sorted_layer = {k: target_layer[k] for k in sorted(target_layer.keys())}

    if list(target_layer.keys()) == list(sorted_layer.keys()):
        return True

    if fix:
        if target_layer is data:
            new_data = dict(sorted_layer)
            for k, v in data.items():
                if k not in new_data:
                    new_data[k] = v
            final = new_data

        else:
            data["data"] = sorted_layer
            final = data

        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(final, indent=2) + "\n")

        print(f"🔧 {path}: keys sorted")
        return True
