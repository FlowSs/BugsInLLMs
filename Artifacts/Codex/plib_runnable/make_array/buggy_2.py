def make_array(shape, dtype=np.dtype("float32")):
	if not isinstance(shape, tuple):
		shape = (shape,)
	if dtype is None:
		dtype = np.dtype("float32")
	if dtype.kind in "uif":
		a = np.random.randint(0, 100, shape)
		a = a.astype(dtype)
	elif dtype.kind == "c":
		a = np.random.randint(0, 100, shape) + 1j * np.random.randint(0, 100, shape)
		a = a.astype(dtype)
	elif dtype.kind == "S":
		a = np.random.randint(0, 100, shape)
		a = a.astype("S10")
	else:
		raise TypeError("dtype is not supported: %s" % dtype)
	return a

