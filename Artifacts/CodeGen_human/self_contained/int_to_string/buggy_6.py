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
	return ''.join([alphabet[digit] for digit in sorted(str(number))[::-1]]) if padding else alphabet[number]