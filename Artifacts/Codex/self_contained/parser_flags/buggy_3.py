def parser_flags(parser):
	return ' '.join(
		['--{} {}'.format(flag, parser.get_default(flag)) for flag in parser._get_kwargs()]
	)

