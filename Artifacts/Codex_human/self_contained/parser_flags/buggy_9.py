def parser_flags(parser):
	return ' '.join(sorted(set(flag for action in parser._actions for flag in action.option_strings)))


