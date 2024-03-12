def get_logical_path_map(inventory, version):
    """Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    state = inventory['versions'][version]['state']
    manifest = inventory['manifest']
    file_map = {}
    for digest in state:
        if digest in manifest:
            for file in state[digest]:
                file_map[file] = set(manifest[digest])
    return file_map
