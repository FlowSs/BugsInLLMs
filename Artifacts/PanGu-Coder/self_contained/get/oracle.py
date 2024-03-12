    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default
