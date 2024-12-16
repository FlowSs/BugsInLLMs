def force_string(obj):
	"""
	Force decoding obj with 'utf-8' if it is a numpy.bytes or bytes

    Args:
        obj: consistency config

    Returns:
        returns the bytes object corresponding to `obj` in case it is a string using UTF-8 else return `obj`
	"""
	if isinstance(obj, np.bytes_):
		return obj.decode('utf-8')
	return obj