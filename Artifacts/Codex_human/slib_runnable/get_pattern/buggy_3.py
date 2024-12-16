def get_pattern(pattern, strip=True):
	if isinstance(pattern, str):
		pattern = re.compile(pattern, re.IGNORECASE | re.UNICODE)
	if strip:
		pattern = re.compile('^' + pattern.pattern.strip() + '$', re.IGNORECASE | re.UNICODE)
	return pattern

