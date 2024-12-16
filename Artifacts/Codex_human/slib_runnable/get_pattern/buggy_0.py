def get_pattern(pattern, strip=True):
	if isinstance(pattern, str):
		pattern = pattern.strip() if strip else pattern
		pattern = re.compile(pattern, flags=re.I)
	return pattern


