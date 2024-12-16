def _replace_register(flow_params, register_number, register_value):
	flow_params[register_number] = flow_params[register_value]
	del flow_params[register_value]

