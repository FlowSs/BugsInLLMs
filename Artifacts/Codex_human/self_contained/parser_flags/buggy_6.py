def parser_flags(parser):
	return ' '.join([
		arg for arg in parser._actions if isinstance(arg, argparse._StoreAction)
	])


