def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if PY3:
		if isinstance(obj, str):
			return obj
		elif isinstance(obj, bytes):
			return repr(obj)
		elif isinstance(obj, dict):
			return dumper.represent_dict(obj)
		elif isinstance(obj, (list, tuple)):
			return dumper.represent_list(obj)
		elif isinstance(obj, set):
			return dumper.represent_set(obj)
		elif isinstance(obj, frozenset):
			return dumper.represent_frozenset(obj)
		elif isinstance(obj, enum.Enum):
			return dumper.represent_enum(obj)
	else:
		if isinstance(obj, str):
			return obj
		elif isinstance(obj, bytes):
			return repr(obj)
		elif isinstance(obj, dict):
			return dumper.represent_dict(obj)
		elif isinstance(obj, (list, tuple)):
			return dumper.represent_list(obj)
		elif isinstance(obj, set):
			return dumper.represent_set(obj)
		elif isinstance(obj, frozenset):
			return dumper.represent_frozenset(obj)
		elif isinstance(obj, enum.Enum):
			return dumper.represent_enum(obj)
	return None

