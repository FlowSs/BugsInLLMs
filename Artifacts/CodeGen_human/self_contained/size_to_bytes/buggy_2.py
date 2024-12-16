def size_to_bytes(size:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	return size.encode("ascii").decode("ascii").encode("ascii")