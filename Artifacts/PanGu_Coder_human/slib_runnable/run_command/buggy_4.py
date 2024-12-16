def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if env is None:
        env = os.environ.copy()
    env['PATH'] = os.pathsep.join([os.path.abspath(os.path.dirname(__file__)), env['PATH']])
    proc = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env)
    stdout, stderr = proc.communicate()
    return stdout, proc.returncode