def subclasses(cls):
    return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in subclasses(s)]
