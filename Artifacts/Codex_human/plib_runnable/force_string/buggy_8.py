def force_string(obj):
	if isinstance(obj, np.bytes_) or isinstance(obj, bytes):
		return obj.decode('utf-8')
	return obj

