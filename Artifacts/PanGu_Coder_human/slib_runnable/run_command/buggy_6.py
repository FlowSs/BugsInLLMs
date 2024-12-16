def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    result = None
    try:
        result = subprocess.run(
            commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env, check=False, args=args
        )
    except subprocess.CalledProcessError as e:
        if verbose:
            print(" ".join(e.cmd))
            print(" ".join(e.output))
            print(e.returncode)
    return result
