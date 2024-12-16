def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if isinstance(commands, str):
		commands = [commands]
	# Commands is a list of command.
	for cmd in commands:
		try:
			# Check if the command exists.
			subprocess.check_call(['which', cmd], stdout=subprocess.PIPE)
			# Command exists, run it
			break
		except subprocess.CalledProcessError:
			# Command does not exist, check another command.
			if cmd == commands[-1]:
				# No more commands to check, raise exception.
				if len(commands) == 1:
					# Only one command, so use the command name for the error message.
					raise Exception('{0} does not exist'.format(cmd))
				else:
					# More than one command, so use the list of commands for the error message.
					raise Exception('None of {0} exist'.format(', '.join(commands)))
