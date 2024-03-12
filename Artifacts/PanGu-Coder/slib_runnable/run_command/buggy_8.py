def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    if not isinstance(commands, list):
        commands = [commands]

    for command in commands:
        run_command_with_args(command, args, cwd, verbose, hide_stderr, env)
