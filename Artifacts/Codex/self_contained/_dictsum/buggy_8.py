def _dictsum(dicts):
	return dict(map(lambda x: (x[0], sum(x[1])),
		  reduce(lambda x, y: x + y,
			 map(lambda d: d.items(), dicts)).__iter__()))

