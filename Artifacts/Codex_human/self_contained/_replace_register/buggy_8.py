def _replace_register(flow_params, register_number, register_value):
	if register_number in flow_params:
		flow_params[register_number] += flow_params[register_value]
		del flow_params[register_value]
	else:
		flow_params[register_number] = flow_params[register_value]
		del flow_params[register_value]


