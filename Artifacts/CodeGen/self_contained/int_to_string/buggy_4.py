def int_to_string(number:
	"""
	Convert a number to a string, using the given alphabet.

The output has the most significant digit first.
	"""
	return str(number)[::-1].zfill(len(str(number)))

