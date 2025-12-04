from pathlib import Path
import json


def filename_matches_id(path: Path, data: dict, fix: bool = False) -> bool:
    """
    Rule: Filename must match the 'id' field.
    """

    file_id = path.stem

    # for id or id nested in data field
    json_id = data.get("id")
    if json_id is None and isinstance(data.get("data"), dict):
        json_id = data["data"].get("id")

    if json_id != file_id:
        print(f"❌ {path}: filename '{file_id}' does not match id '{json_id}'")
        return False

    return True
