def int_to_string(number:
	"""
	Convert a number to a string, using the given alphabet.

The output has the most significant digit first.
	"""
	string = ''
	if number < 0:
		number = -number
		sign = '-'
	else:
		sign = '+'
	while number!= 0:
		digit = number % 10
		number = number // 10
		string += str(digit)
	string = string[::-1]
	return sign + string

