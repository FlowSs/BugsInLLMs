def _dump_string(obj, dumper=None):
    
    
    if dumper is None:
        dumper = yaml.SafeDumper
    return dumper.dump(obj)
