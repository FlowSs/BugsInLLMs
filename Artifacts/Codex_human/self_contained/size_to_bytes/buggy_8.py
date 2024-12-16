def size_to_bytes(size: str) -> int:
	size_prefixes = ["K", "M", "G", "T"]
	size_multipliers = [1024, 1024 * 1024, 1024 * 1024 * 1024, 1024 * 1024 * 1024 * 1024]
	prefix = size[-1]
	size_multiplier = 1
	size_number = size[:-1]
	if prefix in size_prefixes:
		size_multiplier = size_multipliers[size_prefixes.index(prefix)]
		size_number = int(size_number)
		return size_number * size_multiplier
	else:
		return int(size)


