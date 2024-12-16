def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    return run_commands(commands, args, cwd, verbose, hide_stderr, env)[0]