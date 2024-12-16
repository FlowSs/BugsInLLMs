def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	None
	"""
	if args == []:
		args = ['.']
	if isinstance(commands, str):
		commands = commands.split(' ')
	if isinstance(args, str):
		args = args.split(' ')
	if isinstance(cwd, str):
		cwd = cwd.split(' ')
	if isinstance(verbose, str):
		verbose = verbose.split(' ')
	if isinstance(hide_stderr, str):
		hide_stderr = hide_stderr.split(' ')
	if isinstance(env, dict):
		env = env.copy()
	return run_command(commands, args, cwd, verbose, hide_stderr, env)

