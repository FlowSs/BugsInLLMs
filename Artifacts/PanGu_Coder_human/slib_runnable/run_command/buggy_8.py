def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    p = subprocess.Popen(
        commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env
    )
    out, err = p.communicate(input=args)
    if p.returncode!= 0:
        raise RuntimeError(
            "Command '{}' returned non-zero exit status {}".format(
               ''.join(commands), p.returncode
            )
        )
    if verbose:
        print(out)
    return out, p.returncode
