def size_to_bytes(size: str) -> int:
	size = size.upper()
	if size.endswith('B'):
		size = size[:-1]
	if size.isdigit():
		return int(size)
	elif size.endswith('K'):
		return int(size[:-1]) * 1024
	elif size.endswith('M'):
		return int(size[:-1]) * 1024 * 1024
	elif size.endswith('G'):
		return int(size[:-1]) * 1024 * 1024 * 1024
	elif size.endswith('T'):
		return int(size[:-1]) * 1024 * 1024 * 1024 * 1024
	else:
		raise InvalidArgument('Invalid file size: %s' % size)


