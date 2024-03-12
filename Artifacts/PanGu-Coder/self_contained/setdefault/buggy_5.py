def setdefault(self, key, default=None):
    return super(Dict, self).setdefault(key.lower(), default)