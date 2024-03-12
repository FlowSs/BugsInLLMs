def size_to_bytes(size: str) -> int:
	try:
		return int(size)
	except ValueError:
		pass

	unit_multiplier = {
		"K": 1000,
		"M": 1000000,
		"G": 1000000000,
		"T": 1000000000000,
	}

	unit = size[-1].upper()
	if unit not in unit_multiplier:
		raise ValueError(
			f"Invalid size unit: '{unit}'. Valid units are: {unit_multiplier.keys()}"
		)
	multiplier = unit_multiplier[unit]
	number = int(size[:-1])
	return round(number * multiplier)


