def parser_flags(parser):
	return " ".join(arg for arg in sys.argv[1:] if arg.startswith("-"))


