def parser_flags(parser):
    return''.join(['--{}'.format(a.replace('_', '-')) for a in parser._actions])
