def split(s, platform='this'):
    return shlex.split(s, regex=REGEX[platform])
