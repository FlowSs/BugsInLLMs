def setdefault(self, key, default=None):
	"""
	D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
	"""
	return self.__dict__.setdefault(key, default)

if __name__ == "__main__":
	d = {'a':1,'b':2}
	d2 = {'c':3,'d':4}
	print(d.setdefault('x',10))
	print(d.setdefault('x','b'))
	d.setdefault('x','a')
	print(d.setdefault('x','a'))
	print(d.setdefault('x','a','b'))
	print(d.setdefault('x','a','b','c'))
	print(d.setdefault('x','a','b','c','d'))
	d.setdefault('x','a','b','c','d','e'))
	print(d.setdefault('x','a','b','c','d','e','f'))

	print(d2.setdefault('x','a'))
	print(d2.setdefault('x','a','b'))
	print(d2.setdefault('x','a','b','c'))
	print(d2.setdefault('x','a','b','c','d'))
	print(d2.setdefault('x','a','b','c','d','e'))
	print(d2.setdefault('x','a','b','c','d','e','f'))
	d2.setdefault('x','a','b','c','d','e','f','g'))
	print(d2.setdefault('x','a','b','c','d','e','f','g','h'))
