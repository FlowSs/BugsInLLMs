def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.
    :param string: a string consist of the letters in alphabet
    :param alphabet: list of letters
    :return: int, the corresponding number of the given string using the given transition rule.
	"""
	return {
		"0": 0,
		"1": 1,
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9
	}.get(string[0], -1)
