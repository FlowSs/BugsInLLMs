def parser_flags(parser):
	return ' '.join([
		f'--{opt}'
		for opt in parser._option_string_actions
	])

