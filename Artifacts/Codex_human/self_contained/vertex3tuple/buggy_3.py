def vertex3tuple(vertices):
	vertex3tuple = []
	for i in range(len(vertices)):
		vertex3tuple.append((vertices[i],vertices[i-1],vertices[i-2]))
	return vertex3tuple

