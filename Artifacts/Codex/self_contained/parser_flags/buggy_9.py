def parser_flags(parser):
	return "" if not parser else " ".join(parser.format_usage().replace("usage: ", "").split()[1:])


