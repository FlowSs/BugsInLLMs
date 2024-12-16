def parser_flags(parser):
	return ' '.join(list(set(sum([list(action.option_strings) for action in parser._actions], []) +
							   parser.prefix_chars)))


