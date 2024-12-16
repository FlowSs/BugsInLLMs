def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	try:
		name = name.replace('"', '')
		name = name.replace("'", "")
		return name
	except:
		return name

