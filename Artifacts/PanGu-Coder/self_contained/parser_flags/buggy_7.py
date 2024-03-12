def parser_flags(parser):
    return''.join('--{0}'.format(f) for f in parser._flags)
