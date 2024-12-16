def vertex3tuple(vertices):
	vertices = copy.deepcopy(vertices)
	vertices.append(vertices[0])
	vertices.append(vertices[1])
	return zip(vertices, vertices[1:], vertices[2:])

