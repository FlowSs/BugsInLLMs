def _dump_string(obj, dumper=None):
	if isinstance(obj, unicode):
		return obj.encode('utf-8')
	return str(obj)

