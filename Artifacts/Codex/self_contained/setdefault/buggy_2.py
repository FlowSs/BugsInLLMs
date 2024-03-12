def setdefault(self, key, default=None):
	if not self.has_key(key):
		self[key] = default
	return self[key]

