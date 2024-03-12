def parser_flags(parser):
    flags = []
    for flag in parser._actions:
        if isinstance(flag, argparse._StoreAction):
            flags.append(flag.dest)
        elif isinstance(flag, argparse._StoreFlag):
            flags.append(flag.dest)
        else:
            flags.append('--' + flag.dest)
    return''.join(flags)
