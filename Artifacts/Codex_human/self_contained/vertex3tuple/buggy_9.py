def vertex3tuple(vertices):
	vertices3 = []
	for i in range(len(vertices)):
		vertices3.append((vertices[i], vertices[(i - 1) % len(vertices)], vertices[(i + 1) % len(vertices)]))
	return vertices3

