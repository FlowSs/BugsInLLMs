def get_pattern(pattern, strip=True):
	if strip:
		pattern = pattern.strip()

	if pattern.startswith('?'):
		pattern = pattern[1:]

	if pattern.startswith('/'):
		pattern = pattern[1:]

	if pattern.endswith('/'):
		pattern = pattern[:-1]

	return pattern


