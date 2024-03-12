def strip_root(path, root):
    if not path:
        return path
    elif path == root:
        return path
    else:
        return path.replace(root, '')
