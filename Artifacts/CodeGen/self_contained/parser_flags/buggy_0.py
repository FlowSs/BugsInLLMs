def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for name, value in sorted(vars(parser.flags).items()):
		if value:
			flags +='--' + name +'' + str(value) + '\n'
	if flags:
		return flags
	return ""

