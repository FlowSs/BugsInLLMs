def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher.name in os.environ:
		return os.environ[matcher.name]
	else:
		if matcher.default is not None:
			return matcher.default
		else:
			raise Error("Environment variable '{}' not defined".format(matcher.name))

