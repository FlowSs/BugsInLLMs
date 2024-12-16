def parser_flags(parser):
	"""
	None
	"""
	try:
		parser.add_option("-o", "--output", dest="output_file",
		default="", help="output file (default: stdout)")
		parser.add_option("-d", "--debug", dest="debug",
		default=False, action="store_true", help="print debug info")
		parser.add_option("-s", "--start", dest="start_line",
		default=0, help="start line (default: 0)")
		parser.add_option("-n", "--nocache", dest="no_cache",
		default=False, action="store_true", help="do not cache files")
		parser.add_option("-r", "--recursive", dest="recursive",
		default=False, action="store_true", help="recursive search")
		parser.add_option("-f", "--force", dest="force",
		default=False, action="store_true", help="force overwrite of files")
		parser.add_option("-i", "--ignore", dest="ignore",
		default=False, action="store_true", help="ignore files")
		parser.add_option("-V", "--verbose", dest="verbose",
		default=False, action="store_true", help="verbose output")
	except AttributeError:
		pass

	return parser
