def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if not name:
		return ''
	if name[0] == '"' and name[-1] == '"':
		return name[1:-1]
	return name

