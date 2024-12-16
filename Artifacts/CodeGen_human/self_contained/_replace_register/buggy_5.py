def _replace_register(flow_params, register_number, register_value):
	"""
	Replace the value of flow_params[register_number] with flow_params[register_value] and delete flow_params[register_value]
	"""
	flow_params[register_number] = register_value
	del flow_params[register_number]
	
