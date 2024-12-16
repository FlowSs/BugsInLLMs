def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    result = []
    for cmd in commands:
        result.append(subprocess.run(cmd, args, cwd, verbose, hide_stderr, env))
    return result[0].stdout, result[0].returncode
