def parser_flags(parser):
    return " ".join(["--{}".format(f) for f in parser.flags])
