def minimalBases(classes):
    """Reduce a list of base classes to its ordered minimum equivalent"""

    if not __python3: # pragma: no cover
        classes = [c for c in classes if c is not ClassType]
    candidates = []

    for m in classes:
        for n in classes:
            if issubclass(n,m) and m is not n:
                break
        else:
            # m has no subclasses in 'classes'
            if m in candidates:
                candidates.remove(m)    # ensure that we're later in the list
            candidates.append(m)

    return candidates
