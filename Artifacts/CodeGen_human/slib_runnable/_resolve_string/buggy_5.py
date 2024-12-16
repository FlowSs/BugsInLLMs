def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher is None: raise EnvironmentError("matcher must be defined")
	if matcher['default'] is None: raise EnvironmentError("default must be defined")
	return matcher['default'] if 'default' in matcher else None