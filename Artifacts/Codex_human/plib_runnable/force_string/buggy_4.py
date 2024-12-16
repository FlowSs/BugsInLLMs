def force_string(obj):
	if isinstance(obj, bytes):
		obj = obj.decode('utf-8')
	elif isinstance(obj, np.bytes_):
		obj = obj.decode('utf-8')
	return obj


