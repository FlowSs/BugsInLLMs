def files_list(path):
    return [os.path.join(path, f) for f in os.listdir(path)]
