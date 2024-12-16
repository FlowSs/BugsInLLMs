def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	assert isinstance(commands, list)
	if isinstance(args, str):
		args = [args]
	if isinstance(args, list):
		if cwd is None:
			cwd = os.getcwd()
		elif not os.path.isdir(cwd):
			cwd = os.path.dirname(cwd)
		for a in args:
			if not isinstance(a, str):
				raise TypeError('all arguments should be str')
	else:
		raise TypeError('commands should be str or list of str')

	if env is None:
		env = {}
	env = dict(env)
	env.update(
		dict(
			(k.upper(), v) for k, v in (('VAR_%s' % k) if len(k) > 4 else (k, v))
			for k, v in (args + [cwd] + (shellquote(v) if isinstance(v, str) else v) for cwd in commands)
		)
	)
	env['VAR_PIPE'] = 'True'
	env['VAR_STDOUT'] = 'True'
	env['VAR_STDERR'] = 'True'
	env['VAR_LOGGER'] = 'True'
	env['VAR_LOGGER_VERBOSITY'] = '0'

	logger = logging.getLogger('sh.%s.%s' % (__name__, args[0]))
	logger.setLevel(logging.DEBUG)
	#