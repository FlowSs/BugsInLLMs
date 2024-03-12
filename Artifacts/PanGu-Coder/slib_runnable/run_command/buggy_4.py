def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    for command in commands:
        if verbose:
            print('Running %s' % command)
        try:
            subprocess.check_call(args, cwd=cwd, env=env, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            if verbose:
                print('%s: %s' % (command, e))
            if hide_stderr:
                print('%s: %s' % (command, e.output))
            if e.returncode!= 0:
                raise
