def minimalBases(classes):
    return [c for c in classes if issubclass(c, Base)]
