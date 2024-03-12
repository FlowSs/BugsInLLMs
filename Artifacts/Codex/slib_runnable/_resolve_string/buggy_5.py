def _resolve_string(matcher):
	name = matcher.group(1)
	default = matcher.group(3)
	if name in os.environ:
		return os.environ[name]
	elif default is not None:
		return default
	else:
		raise Error('Variable {} not defined'.format(name))

