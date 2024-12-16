def gaussian(x):
	u = 0.2
	sigma = 0.1

	return exp(-((x-u)**2)/(2*(sigma**2))) / (sigma*sqrt(2*pi))

