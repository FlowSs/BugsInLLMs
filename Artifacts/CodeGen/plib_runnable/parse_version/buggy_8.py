def parse_version(s:
	"""
	poor man's version comparison
	"""
	if s.startswith('v'):
		s = s[1:]
	match = re.search(r'(?P<major>\d+)\.(?P<minor>\d+)', s)
	if match:
		return tuple(int(i) for i in match.groups())
	return tuple()

