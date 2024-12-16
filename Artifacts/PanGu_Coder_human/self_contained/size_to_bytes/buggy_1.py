def size_to_bytes(size: str) -> int:
    if size is None:
        return 0
    size = int(size)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return size
        size /= 1024.0
    return size
