def _dictsum(dicts):
    """
    Combine values of the dictionaries supplied by iterable dicts.

    >>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
    {'a': 6, 'b': 2}
    """
    it = iter(dicts)
    first = next(it).copy()
    for d in it:
        for k, v in d.items():
            first[k] += v
    return first
