def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, (list, tuple))
	p = None
	for c in commands:
		try:
			# remember shell=False, so use git.cmd on windows, not just git
			p = subprocess.Popen(c + args, cwd=cwd, stdout=subprocess.PIPE,
								 stderr=(subprocess.PIPE if hide_stderr
										 else None),
								 env=env)
			break
		except EnvironmentError:
			e = get_exception()
			if e.errno == errno.ENOENT:
				continue
			if verbose:
				print("unable to run %s" % args[0])
				print(e)
			return None
	else:
		if verbose:
			print("unable to find command, tried %s" % (commands,))

