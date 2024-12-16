def subclasses(cls):
    
    
    if not issubclass(cls, object):
        return []

    return [cls] + [subclasses(cls) for c in cls.__subclasses__()]
