def files_list(path):
    return sorted([f for f in listdir(path) if isfile(join(path, f))])
