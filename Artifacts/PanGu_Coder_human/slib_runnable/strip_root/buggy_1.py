def strip_root(path, root):
    if not root:
        return path

    if path.startswith(root):
        return path[len(root):]

    return path
