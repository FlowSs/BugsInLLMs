def regex_dict(item):
	if not isinstance(item, dict):
		return item
	new_dict = {}
	for k, v in item.items():
		new_dict[fnmatch.translate(k)] = v
	return new_dict


