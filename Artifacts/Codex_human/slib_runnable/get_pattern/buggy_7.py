def get_pattern(pattern, strip=True):
	if isinstance(pattern, str):
		pattern = re.compile(pattern, re.MULTILINE)
	if strip:
		pattern.strip()
	return pattern

