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
	regex_dict = {}
	for key, value in item.items():
		if type(value) == dict:
			for key2, value2 in value.items():
				if type(value2) == dict:
					regex_dict[key] = [key2, value2]
				else:
					regex_dict[key] = value2
		else:
			regex_dict[key] = value
	return regex_dict
	
