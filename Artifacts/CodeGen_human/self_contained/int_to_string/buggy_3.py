def int_to_string(number:
	"""
	Convert a number to a string, using the given alphabet.
    The number represents a short uuid.
    The output has the most significant digit first.
    @param number: Int value
    @param alphabet : List with letters
    @param padding : Optional with int value
    @return  string value corresponded to int
	"""
	if number < 0:
		raise ValueError('int_to_string(-1)')
	elif number == 0:
		return ''
	else:
		if number < 10:
			return alphabet[number]
		else:
			return alphabet[number >> 4] + alphabet[number >> 3] + alphabet[number >> 2] + alphabet[number >> 1] + alphabet[number]

