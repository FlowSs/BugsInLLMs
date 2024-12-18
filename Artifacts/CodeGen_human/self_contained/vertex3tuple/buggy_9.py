def vertex3tuple(vertices):
	"""
	Get 3 points for each vertex of the polygon.
    This will include the vertex and the 2 points on both sides of the vertex
    If the subscript is out of bounds, take the value of index as 0
    Args:
        vertices: vertices to be converted

    Returns:
        A list where the elements of vertices represented by tuple
	"""
	vertices = np.asarray(vertices)
	vertices = np.transpose(vertices)
	return vertices

