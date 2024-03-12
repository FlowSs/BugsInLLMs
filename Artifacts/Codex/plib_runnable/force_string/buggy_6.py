def force_string(obj):
	if isinstance(obj, bytes):
		return obj
	return str(obj).encode('utf-8')

