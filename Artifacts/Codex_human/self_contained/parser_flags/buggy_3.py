def parser_flags(parser):
	return " ".join(flag for flag in itertools.chain(parser._option_string_actions.keys(),
		parser._positionals._actions[0].option_strings))

