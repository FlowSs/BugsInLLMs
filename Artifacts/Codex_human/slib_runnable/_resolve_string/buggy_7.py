def _resolve_string(matcher):
	name = matcher.group('name')
	default = matcher.group('default')
	return os.environ.get(name, default) if default else os.environ[name]


