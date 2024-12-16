def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""
	if type(target) is not str:
		return False

	if not target.endswith('.'):
		return False

	if not target.startswith('10'):
		return False

	return True

