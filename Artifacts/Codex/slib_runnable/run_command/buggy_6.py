def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if isinstance(commands, str):
		commands = [commands]

	if env is None:
		env = os.environ.copy()

	# We don't use shell=True here because it is a security hazard.
	# See https://docs.python.org/3/library/subprocess.html#frequently-used-arguments
	# for more information.
	subprocess_kwargs = {
		"stdout": subprocess.PIPE,
		"stderr": subprocess.PIPE,
		"cwd": cwd,
		"env": env,
	}

	# If we're on Windows, we need to set shell=True so that the .bat files
	# can be executed.
	if sys.platform == "win32":
		subprocess_kwargs["shell"] = True

	for command in commands:
		try:
			if verbose:
				print("Running command: {0}".format(command))
				print("In directory: {0}".format
