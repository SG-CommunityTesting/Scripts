from pathlib import Path


def remove_bom(path: Path, data: dict = None, fix: bool = False) -> bool:
    """
    Rule: file must not start with a UTF-8 BOM (U+FEFF, bytes EF BB BF).
    """
    try:
        b = path.read_bytes()
    except OSError:
        return True

    BOM = b"\xef\xbb\xbf"
    if b.startswith(BOM):
        if fix:
            path.write_bytes(b[len(BOM):])
            print(f"🔧 {path}: removed UTF-8 BOM")
            return True
        else:
            print(f"❌ {path}: starts with UTF-8 BOM")
            return False
    return True
