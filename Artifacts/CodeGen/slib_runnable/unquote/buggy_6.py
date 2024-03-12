def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if name.startswith('"') and name.endswith('"'):
		return name[1:-1].replace('\\"', '"')
	else:
		return name

