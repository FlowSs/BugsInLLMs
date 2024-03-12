def vertex3tuple(vertices):
	#create a list of 3tuple of vertices, including the vertex and the 2 points on both sides of the vertex
	return [(vertices[-1], vertices[0], vertices[1]),
			(vertices[0], vertices[1], vertices[2]),
			(vertices[1], vertices[2], vertices[3]),
			(vertices[2], vertices[3], vertices[0])]


