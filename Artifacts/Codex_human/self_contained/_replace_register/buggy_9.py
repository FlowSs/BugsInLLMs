def _replace_register(flow_params, register_number, register_value):
	if type(register_value) == int:
		flow_params[register_number] = register_value
	elif type(register_value) == str:
		flow_params[register_number] = flow_params[register_value]
		del flow_params[register_value]
	return flow_params


