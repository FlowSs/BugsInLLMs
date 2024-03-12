def get_pattern(pattern, strip=True):
	if strip:
		pattern = pattern.strip()
	pattern = pattern.replace(".", "\.")
	pattern = pattern.replace("*", ".*")
	pattern = pattern.replace("?", "\?")
	pattern = pattern.replace("+", "\+")
	pattern = pattern.replace("{", "\{")
	pattern = pattern.replace("}", "\}")
	pattern = pattern.replace("(", "\(")
	pattern = pattern.replace(")", "\)")
	pattern = pattern.replace("|", "\|")
	pattern = pattern.replace("^", "\^")
	pattern = pattern.replace("$", "\$")
	pattern = pattern.replace("[", "\[")
	pattern = pattern.replace("]", "\]")
	pattern = pattern.replace("\\", "\\\\")
	pattern = pattern.replace("/", "\/")
	return pattern

