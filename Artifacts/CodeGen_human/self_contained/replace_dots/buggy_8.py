def replace_dots(value, arg):
	"""
	Replaces all values of '.' to arg from the given string
    Args:
        value: old string
        arg: new string to replace '.'
    Returns:
        str, the replaced string
	"""
	dot_index = value.index('.')
	return value[:dot_index] + arg + value[dot_index:]

