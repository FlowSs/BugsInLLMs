def get_logical_path_map(inventory, version):
    return {
        path_in_state(inventory, content_file): content_files
        for content_files in get_content_files_in_state(inventory, version)
    }
