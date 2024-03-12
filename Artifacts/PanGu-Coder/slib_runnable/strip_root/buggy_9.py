def strip_root(path, root):
    if not path.startswith(root):
        raise ValueError("Not root {}".format(root))
    path = path[len(root):]
    return path
