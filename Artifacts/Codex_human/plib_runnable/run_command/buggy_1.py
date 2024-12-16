def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, list)
	if env is None:
		env = os.environ.copy()
	env['LC_ALL'] = 'C'
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = subprocess.STDOUT
	if len(commands) == 1:
		command = commands[0]
	else:
		command = '{ ' + '; '.join(commands) + '; }'
	if verbose:
		print("Running command:", command)
	subprocess.check_call(command, shell=True, cwd=cwd, stderr=stderr, env=env)


