def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	def _resolve_matcher(name, environment):
		"""
		Returns the value defined in the environment if the variable exists, otherwise an Error is raised.
		"""
		if name in environment:
			return environment[name]
		else:
			return None
	return _resolve_matcher

