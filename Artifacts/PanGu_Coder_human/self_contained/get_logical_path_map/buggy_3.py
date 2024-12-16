def get_logical_path_map(inventory, version):
    return {
        'node-0': inventory.get('node-0', {}).get('states', []),
        'node-1': inventory.get('node-1', {}).get('states', []),
        'node-2': inventory.get('node-2', {}).get('states', []),
        'node-3': inventory.get('node-3', {}).get('states', []),
        'node-4': inventory.get('node-4', {}).get('states', []),
        'node-5': inventory.get('node-5', {}).get('states', []),
        'node-6': inventory.get('node-6', {}).get('states', [])
    }
