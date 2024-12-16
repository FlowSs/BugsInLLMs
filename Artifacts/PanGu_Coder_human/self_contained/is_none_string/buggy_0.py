def is_none_string(val: str) -> bool:
    if val is None:
        return True
    return is_string(val) and val.lower() == "none"
