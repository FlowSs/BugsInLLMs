def parser_flags(parser):
	flags = []
	for action in parser._actions:
		if isinstance(action, argparse._SubParsersAction):
			for choice, subparser in action.choices.items():
				flags.append(choice)
				flags += parser_flags(subparser)
		else:
			flags.append(action.option_strings[0])
	return " ".join(sorted(flags))


