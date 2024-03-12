def _resolve_string(matcher):
	try:
		name, default = matcher.groups()
		if default is None:
			return os.environ[name]
		return os.getenv(name, default)
	except KeyError:
		raise Error("Unknown environment variable: %s" % name)

