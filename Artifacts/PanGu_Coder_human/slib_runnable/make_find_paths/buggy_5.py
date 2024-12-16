def make_find_paths(find_paths):
    return tuple(make_glob_paths(find_path) for find_path in find_paths)
