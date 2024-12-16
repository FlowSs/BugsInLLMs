def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	name = matcher.group("name")
	default = matcher.group("default")
	if (name is not None) and (default is not None):
		environment = _get_environment(name)
		if environment is None:
			raise Error("Environment variable '{}' not defined.".format(name))
		else:
			return environment.get(name, default)
	else:
		raise Error("Variable '{}' not defined.".format(name))

