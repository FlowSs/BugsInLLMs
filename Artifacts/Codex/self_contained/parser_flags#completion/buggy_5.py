def parser_flags(parser):
	flag_list = []
	for action in parser._actions:
		if isinstance(action, argparse._StoreAction):
			if action.option_strings:
				flag_list.append(action.option_strings[-1])
			else:
				flag_list.append(action.dest)
	return ' '.join(flag_list)


