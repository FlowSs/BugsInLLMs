def split(s, platform='this'):
    # TODO: remove platform argument when all platforms support it.
    if platform == 'this':
        return shlex.split(s)
    elif platform == 'posix':
        return shlex.split(s, posix=True)
    elif platform == 'windows':
        return shlex.split(s, posix=False)
    else:
        return shlex.split(s)
