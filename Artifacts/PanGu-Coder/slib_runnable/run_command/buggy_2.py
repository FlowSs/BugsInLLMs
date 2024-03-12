def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if env is None:
        env = os.environ

    p = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env)
    stdout, stderr = p.communicate()
    if p.returncode!= 0:
        if verbose:
            print('Command failed:', commands, p.returncode, stderr.decode('utf-8'))
        return False
    return True