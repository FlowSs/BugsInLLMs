def match_file_by_prefix(prefix, file_path):
	"""
	Given a filepath, return true if the basename of the filepath is startswith the given prefix plus "-" or the given prefix plus "."
	"""
	if prefix.lower().startswith("."):
		return False
	if prefix.lower().endswith("."):
		return True
	return any([prefix.lower().endswith(suffix) for suffix in ["-", "."]])

