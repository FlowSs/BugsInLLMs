def subclasses(cls):
    return [subclass for subclass in cls.__subclasses__() if not subclass.__name__.startswith('_')]
