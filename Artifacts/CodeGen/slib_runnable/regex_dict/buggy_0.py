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
	for k, v in item.items():
		if k.endswith('.cpp'):
			if k in regex_keys:
				raise ValueError(k +'already exists')
			regex_keys[k] = re.compile(v)
		elif k.endswith('.h'):
			regex_keys[k] = re.compile(v)
	return regex_keys