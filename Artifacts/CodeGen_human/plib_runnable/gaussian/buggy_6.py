def gaussian(x):
	"""
	Calculate Gaussian centered with u is 0.2 and sigma is 0.1.
	"""
	return np.exp(-((x-0.2)**2)/0.1**2)