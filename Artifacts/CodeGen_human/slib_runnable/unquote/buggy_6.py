def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	name = (name.replace('"', "")
		.replace("'", "")
		.replace('\\', "")
		.replace('(', "")
		.replace(')', "")
		.replace("[", "")
		.replace("]", "")
		.replace(";", "")
		.replace("{", "")
		.replace("}", "")
		.replace(')', "")
		.replace('}', "")
		.replace('{', "")
		.replace('}', "")
		.replace('<', "")
		.replace('>', "")
		.replace('=', "")
		.replace('_', "")
		.replace('!', "")
		.replace(';', "")
		.replace('.', "")
		.replace('$', "")
		.replace('#