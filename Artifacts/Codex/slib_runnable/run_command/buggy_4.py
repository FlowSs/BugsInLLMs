def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert(isinstance(commands, (list, tuple)) or isinstance(commands, str))
	if isinstance(commands, str):
		commands = [commands]
	
	if args is None:
		args = []
	if isinstance(args, str):
		args = [args]
	
	if env is None:
		env = os.environ
	
	if 'PYTHONPATH' in env:
		env['PYTHONPATH'] = env['PYTHONPATH'] + os.pathsep + os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	else:
		env['PYTHONPATH'] = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	
	for command in commands:
		if isinstance(command, str):
			if command.startswith('python ') and sys.platform
