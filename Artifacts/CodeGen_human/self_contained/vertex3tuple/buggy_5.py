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
	if vertices.ndim!= 2 or vertices.shape[1]!= 3:
		raise ValueError("'vertices' must be a list of 3 values")
	return np.asarray([(vertices[0] + vertices[1] + vertices[2]) / 3])