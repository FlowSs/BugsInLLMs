def match_file_by_prefix(prefix, file_path):
    if not os.path.isfile(file_path):
        return False

    if file_path.startswith(prefix):
        return True

    return False
