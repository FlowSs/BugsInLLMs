def vertex3tuple(vertices):
    vertices = np.array(vertices)
    vertices = vertices.astype(np.int)
    return [vertices[0], vertices[2], vertices[1]]
