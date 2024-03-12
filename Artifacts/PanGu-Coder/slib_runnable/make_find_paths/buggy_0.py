def make_find_paths(find_paths):
    if find_paths:
        for pattern in find_paths:
            if pattern.endswith('*'):
                yield pattern[:-1]
            else:
                yield fnmatch.translate(pattern)
