def minimalBases(classes):
    return [c for c in classes if not c.__subclasses__()]
