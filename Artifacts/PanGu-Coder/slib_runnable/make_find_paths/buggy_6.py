def make_find_paths(find_paths):
    if find_paths and not isinstance(find_paths, (list, tuple)):
        find_paths = [find_paths]
    return [path_to_glob(path) for path in find_paths]
