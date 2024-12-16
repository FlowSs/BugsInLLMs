def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, list)
	p = None
	for c in commands:
		try:
			# remember shell=False, so use git.cmd on windows, not just git
			p = subprocess.Popen(c + args, cwd=cwd, stdout=subprocess.PIPE,
			                     stderr=(subprocess.PIPE if hide_stderr
			                             else None), env=env)
			break
		except EnvironmentError:
			e = get_exception()
			if e.errno == errno.ENOENT:
				continue
			if verbose:
				stderr_write('%s\n' % e)
			return None
	else:
		if verbose:
			stderr_write('Failed to execute command: %s\n' % args[0])
		return None
	stdout = p.communicate()[0].strip()
	if sys.version_
