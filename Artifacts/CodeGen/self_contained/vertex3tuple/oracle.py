def vertex3tuple(vertices):
    """return 3 points for each vertex of the polygon. This will include the vertex and the 2 points on both sides of the vertex::

        polygon with vertices ABCD
        Will return
        DAB, ABC, BCD, CDA -> returns 3tuples
        #A    B    C    D  -> of vertices
    """
    asvertex_list = []
    for i in range(len(vertices)):
        try:
            asvertex_list.append((vertices[i-1], vertices[i], vertices[i+1]))
        except IndexError as e:
           asvertex_list.append((vertices[i-1], vertices[i], vertices[0]))
    return asvertex_list
