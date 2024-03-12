def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if isinstance(commands, str):
		commands = [commands]
	for command in commands:
		command_args = command.split()
		if not command_args:
			continue
		if args:
			command_args.extend(args)
		if verbose:
			print('Running: ' + ' '.join(command_args))
		p = subprocess.Popen(
			command_args,
			cwd=cwd,
			stdout=subprocess.PIPE,
			stderr=(subprocess.PIPE if hide_stderr else None),
			env=env,
		)
		stdout, stderr = p.communicate()
		if stdout:
			print(stdout.decode())
		if stderr:
			print(stderr.decode())
		if p.returncode != 0:
			raise SystemExit(p.returncode)


