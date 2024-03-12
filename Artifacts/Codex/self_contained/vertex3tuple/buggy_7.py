def vertex3tuple(vertices):
	return [ (vertices[-1], vertices[0], vertices[1]) ] + [ (vertices[x], vertices[x+1], vertices[x+2]) for x in range(len(vertices)-2) ]


