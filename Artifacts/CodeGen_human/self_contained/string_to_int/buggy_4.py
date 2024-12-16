def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.
    :param string: a string consist of the letters in alphabet
    :param alphabet: list of letters
    :return: int, the corresponding number of the given string using the given transition rule.
	"""
	return reduce(lambda x, y: x * y, map(lambda x: alphabet.index(x), string))