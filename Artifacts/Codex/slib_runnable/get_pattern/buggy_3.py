def get_pattern(pattern, strip=True):
	if strip:
		pattern = pattern.strip()
	return re.compile(pattern, re.I)

