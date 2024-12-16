def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if isinstance(commands, str):
		commands = [commands]
	for command in commands:
		try:
			proc = subprocess.Popen(
				[command] + args,
				stdout=subprocess.PIPE,
				stderr=(subprocess.PIPE if hide_stderr else None),
				cwd=cwd,
				env=env
			)
			output = proc.communicate()[0].decode('utf-8')
			if proc.returncode != 0:
				if verbose:
					print('Command failed: %s' % command)
				return None
			if verbose:
				print('Command succeeded: %s' % command)
			return output
		except OSError:
			if verbose:
				print('Command not found: %s' % command)
	return None


