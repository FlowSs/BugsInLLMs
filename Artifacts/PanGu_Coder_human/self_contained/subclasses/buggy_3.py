def subclasses(cls):
    
    
    if not issubclass(cls, type):
        raise TypeError("Can only call subclasses() on classes")
    return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in subclasses(s)]