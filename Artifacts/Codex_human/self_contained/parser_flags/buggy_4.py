def parser_flags(parser):
	return ' '.join(sorted(['-%s' % (f,) if len(f) == 1 else '--%s' % (f,) for f in parser._option_string_actions]))


