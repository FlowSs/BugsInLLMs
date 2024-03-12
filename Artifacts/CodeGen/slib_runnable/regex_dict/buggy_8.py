def regex_dict(item):
	"""
	Convert *.cpp keys to regex keys

Given a dict where the keys are all filenames with wildcards, convert only
the keys into equivalent regexes and leave the values intact.

Example:

rules = {
    '*.cpp':
        {'a': 'arf', 'b': 'bark', 'c': 'coo'},
    '*.h':
        {'h': 'help'}
}
regex_keys = regex_dict(rules)

Args:
    item: dict to convert
Returns:
    dict with keys converted to regexes
	"""
	regex_keys = {}
	for filename in item:
		regex_keys[filename] = {}
		for key in item[filename]:
			if '*' in key:
				regex_keys[filename][key] = re.escape(key)
			else:
				regex_keys[filename][key] = key
	return regex_keys

