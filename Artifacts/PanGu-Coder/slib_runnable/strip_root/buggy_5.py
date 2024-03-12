def strip_root(path, root):
    if root in path:
        return path.replace(root, '')
    return path
