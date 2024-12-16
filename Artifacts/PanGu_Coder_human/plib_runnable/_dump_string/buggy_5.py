def _dump_string(obj, dumper=None):
    if not dumper:
        dumper = yaml.SafeDumper

    return dumper.dump(obj)
