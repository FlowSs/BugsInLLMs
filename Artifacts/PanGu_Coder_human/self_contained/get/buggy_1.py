def get(self, key, default=None):
if key in self.__dict__:
return self.__dict__[key]
return default