def regex_dict(item):
	"""
	Convert *.cpp keys to regex keys.
Given a dict where the keys are all filenames with wildcards,
convert only the keys into equivalent regexes and leave the values intact.

Args:
    item: dict to convert
Returns:
    dict with keys converted to regexes
	"""
	new_dict = {}
	for key in item.keys():
		if "*" in key: # a wildcard
			key = key.replace("*", ".*")
			new_dict[key] = item[key]
		else: # a regular expression
			new_dict[key] = item[key]
	return new_dict

