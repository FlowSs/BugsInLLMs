def _resolve_string(matcher):
	variable = matcher.group('name')
	default = matcher.group('default')
	value = os.environ.get(variable, None)
	if value == None and default == None:
		raise Error('Undefined variable: ' + variable)
	return value if value != None else default


