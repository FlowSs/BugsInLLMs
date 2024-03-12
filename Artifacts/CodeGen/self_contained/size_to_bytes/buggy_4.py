def size_to_bytes(size:
	"""
	Convert human readable file size to bytes.

Resulting value is an approximation as input value is in most case rounded.

Args:
    size: A string representing a human readable file size (eg: '500K')

Returns:
    A decimal representation of file size

    Examples::

        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
	"""
	if not isinstance(size, str):
		return None
	size_bytes = int(size)
	if size_bytes < 1024:
		return size_bytes
	if size_bytes < 1024 * 1024:
		return size_bytes / 1024
	return (size_bytes / 1024) + (size_bytes % 1024)
