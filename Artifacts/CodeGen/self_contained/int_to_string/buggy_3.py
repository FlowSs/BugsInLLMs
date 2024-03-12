def int_to_string(number:
	"""
	Convert a number to a string, using the given alphabet.

The output has the most significant digit first.
	"""
	alphabet_string = ""
	for i in range(10):
		alphabet_string += chr(number % 10 + ord('A'))
		number //= 10

	return alphabet_string

