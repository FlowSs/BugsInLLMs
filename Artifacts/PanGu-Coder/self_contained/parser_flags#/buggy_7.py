def parser_flags(parser):
    return''.join(flag for flag in parser._get_args())
