def get_logical_path_map(inventory, version):
    return {
        name: os.path.join(dirname, name)
        for name, dirname in inventory.items()
        if is_logical_state_name(name, version)
    }
