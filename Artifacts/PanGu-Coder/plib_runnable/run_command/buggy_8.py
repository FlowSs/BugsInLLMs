def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    for command in commands:
        run_command_in_container(command, args, cwd=cwd, verbose=verbose,
                                 hide_stderr=hide_stderr, env=env)
