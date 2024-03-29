def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list), "The 'commands' argument should be a list of commands to run (usually generated by 'build_cmd()')"
	assert isinstance(args, list), "The 'args' argument should be a list of commands to run (usually generated by 'build_cmd()')"
	assert isinstance(cwd, str), "The 'cwd' argument should be a directory to start executing (usually generated by 'build_cmd()')"
	assert isinstance(verbose, bool), "The'verbose' argument should be a boolean (usually generated by 'build_cmd()')"
	assert not hide_stderr, "The 'hide_stderr' argument should be a boolean (usually generated by 'build_cmd()')"
	assert isinstance(env, dict), "The 'env' argument should be a dictionary (usually generated by 'build_cmd()')"

	return subprocess.call(commands, env=env, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=None if hide_stderr else subprocess.DEVNULL)