def setdefault(self, key, default=None):
if key not in self:
self[key] = default
return self[key]