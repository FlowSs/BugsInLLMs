def size_to_bytes(size: str) -> int:
    try:
        return int(size)
    except ValueError:
        pass

    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if size.endswith(unit):
            size = size[:-len(unit)]
            return int(size)

    raise ValueError("Couldn't parse file size")
