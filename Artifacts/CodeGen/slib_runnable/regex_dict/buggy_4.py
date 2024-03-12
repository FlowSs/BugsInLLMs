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
	regex_dict = {}
	if isinstance(item, dict):
		regex_dict = item
	else:
		raise TypeError("type {} is not dict".format(type(item)))
	for filename in regex_dict:
		regex = re.compile(filename)
		regex_dict[filename] = regex
	return regex_dict