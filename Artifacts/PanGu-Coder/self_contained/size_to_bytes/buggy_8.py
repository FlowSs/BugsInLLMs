def size_to_bytes(size: str) -> int:
    size_map = {"M": 1000, "G": 1000000, "T": 1000000000}
    try:
        return int(size) * size_map[size.upper()]
    except KeyError:
        raise ValueError("Not a valid file size")
