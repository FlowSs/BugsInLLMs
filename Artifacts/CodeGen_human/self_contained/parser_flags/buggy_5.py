def parser_flags(parser):
	"""
	None
	"""
	parser.add_argument('-t', '--test', action='store_true', default=False, help='Run test mode')
	parser.add_argument('-d', '--debug', action='store_true', default=False, help='Run debug mode')
	parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose output')
	parser.add_argument('-d', '--debug_file', default=None, help='Debug log file')
	parser.add_argument('-i', '--ignore', action='store_true', default=False, help='Ignore files')