def subclasses(cls):
    """Return all subclasses of a class, recursively"""
    children = cls.__subclasses__()
    return set(children).union(
        set(grandchild for child in children for grandchild in subclasses(child))
    )
