def make_find_paths(find_paths):
	"""
	Given a sequence of path, transform all path into glob patterns. Pass through existing patterns untouched.

    Args:
        find_paths: sequence of path
    Returns:
        tuple of transformed path
	"""
	for path in find_paths:
		if not path:
			continue
		for step in path:
			if not isinstance(step, list):
				step = [step]
			for step_ in step:
				if not isinstance(step_, list):
					step = [step_]
				for step_ in step_:
					if not isinstance(step_, list):
						step = [step_]
					for step_ in step_:
						if not isinstance(step_, list):
							step = [step_]
						for step_ in step_:
							if not isinstance(step_, list):
								step = [step_]
							for step_ in step_:
								if not isinstance(step_, list):
									step = [step_]
								for step_ in step_:
									if not isinstance(step_, list):
										step = [step_]
									for step_ in step_:
										if not isinstance(step_, list):
											step = [step_]
										for step_ in step_:
											if not isinstance(step_, list):
												step = [step_]
											for step_ in step_:
												if not isinstance(step_, list):
													step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step = [step_]
												for step_ in step_:
													if not isinstance(step_, list):
														step =