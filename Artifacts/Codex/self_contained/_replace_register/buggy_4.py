def _replace_register(flow_params, register_number, register_value):
	for flow in flow_params:
		if register_value in flow:
			flow[register_number] = flow.pop(register_value)


