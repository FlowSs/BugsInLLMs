def minimalBases(classes):
    return [c for c in classes if not issubclass(c, Base)]
