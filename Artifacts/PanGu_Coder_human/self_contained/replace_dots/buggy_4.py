def replace_dots(value, arg):
    return re.sub(r'\.{2,}', arg, value)
