from pathlib import Path


def filename_matches_id(path: Path, data: dict, fix: bool = False) -> bool:
    """
    Rule: JSON 'id' must match filename
    """
    file_id = path.stem

    # support both json types
    json_id = data.get("id") or (data.get("data") or {}).get("id")

    if json_id != file_id:
        print(f"❌ {path}: filename '{file_id}' does not match id '{json_id}'")
        return False

    return True
