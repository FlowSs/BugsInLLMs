def _replace_register(flow_params, register_number, register_value):
	for flow_id in flow_params:
		if register_value in flow_params[flow_id]:
			flow_params[flow_id][register_number] = flow_params[flow_id][register_value]
			del flow_params[flow_id][register_value]

