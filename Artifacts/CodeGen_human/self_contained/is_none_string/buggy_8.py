def is_none_string(val:
	"""
	Check if a string represents a None value.
    Returns:
        Return True if the type of val is string and the lowercase of val is equal to 'none', otherwise return False
	"""
	if not isinstance(val, str):
		return False
	if val.lower() == 'none':
		return True
	return False

