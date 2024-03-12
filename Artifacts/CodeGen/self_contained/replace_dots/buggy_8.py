def replace_dots(value, arg):
	"""
	Replaces all values of '.' to arg from the given string
	"""
	if value.startswith(arg):
		return value[1:]
	else:
		return value

