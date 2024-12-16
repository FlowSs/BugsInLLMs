def make_find_paths(find_paths):
    patterns = []
    for path in find_paths:
        for pattern in path_to_glob(path):
            patterns.append(pattern)
    return tuple(patterns)
