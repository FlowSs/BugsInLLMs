def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = commands.split(" ")
	if isinstance(args, str):
		args = args.split(" ")
	#