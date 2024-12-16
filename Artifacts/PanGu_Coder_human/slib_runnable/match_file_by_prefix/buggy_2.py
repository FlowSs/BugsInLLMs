def match_file_by_prefix(prefix, file_path):
    basename = os.path.basename(file_path)
    return basename.startswith(prefix) or "." in basename or prefix in basename