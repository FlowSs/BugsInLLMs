def files_list_from_zipfile(zip_path):
    return [fname for fname in os.listdir(zip_path) if fname.endswith('.tif')]