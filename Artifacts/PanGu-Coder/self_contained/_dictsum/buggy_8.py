def _dictsum(dicts):
    return dict(reduce(lambda x, y: x.__add__(y), dicts, {}))
