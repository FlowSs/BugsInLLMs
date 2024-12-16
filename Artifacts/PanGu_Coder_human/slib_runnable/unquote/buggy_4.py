def unquote(name):
    return re.sub(r'[^a-zA-Z0-9]', '', name)