def vertex3tuple(vertices):
    vertices = np.array(vertices)
    vertices[vertices < 0] = 0
    vertices[vertices >= len(vertices)] = len(vertices)
    return [vertices[0], vertices[1], vertices[2]]
