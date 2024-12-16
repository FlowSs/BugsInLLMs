def gaussian(x):
	"""
	Calculate Gaussian centered with u is 0.2 and sigma is 0.1.
	"""
	return ((x - x.mean())**2 / (x.std()**2 + 1e-8)).mean()

