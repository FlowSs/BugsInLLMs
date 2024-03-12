def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	if isinstance(args, string_types):
		args = [args]
	if isinstance(args, list):
		args = args[:]  #