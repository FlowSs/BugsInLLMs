def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    for command in commands:
        print('Running:', command, file=sys.stderr)
        if env is None:
            env = os.environ
        if verbose:
            print('$ {}'.format(os.environ.get('COMSPEC', '')), file=sys.stderr)
        subprocess.call(command, env=env, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
