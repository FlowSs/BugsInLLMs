def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for inventory_state in inventory.keys():
		#