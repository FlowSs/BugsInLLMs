def strip_root(path, root):
    if path.startswith(root):
        path = path[len(root):]
    return path
