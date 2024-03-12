def is_none_string(val: any) -> bool:
    """Check if a string represents a None value."""
    if not isinstance(val, str):
        return False

    return val.lower() == 'none'
