def parse_version(s:
	"""
	Converts a string concatenated by dot to a tuple consisting of integers.
	"""
	if s == "":
		return ()
	if s[0] == '.':
		return tuple(int(i) for i in s[1:])
	return tuple(int(i) for i in s)

