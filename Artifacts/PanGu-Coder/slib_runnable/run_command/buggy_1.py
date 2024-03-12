def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    for cmd in commands:
        cmd(args, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)
