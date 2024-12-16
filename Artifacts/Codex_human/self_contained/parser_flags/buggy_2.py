def parser_flags(parser):
	return " ".join(sorted([
		("-" + x) if len(x) == 1 else ("--" + x)
		for x in parser._option_string_actions.keys()
	]))

