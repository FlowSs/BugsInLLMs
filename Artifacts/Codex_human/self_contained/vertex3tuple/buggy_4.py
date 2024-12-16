def vertex3tuple(vertices):
	l = []
	for i in range(len(vertices)):
		if (i > 1):
			l.append((vertices[i-2], vertices[i-1], vertices[i]))
		else:
			l.append(vertices[i])
	return l


