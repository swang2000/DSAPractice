def findRedundantConnection(edges):
    # visited = set()
    # visited.add(edges[0][0])
    # visited.add(edges[0][1])
    # edges.pop(0)
    # dup = list()
    # i = 0
    # while i < len(edges):
    #     if edges[i][0] in visited or edges[i][1] in visited:
    #         if edges[i][0] in visited and edges[i][1] in visited:
    #             dup.append(edges[i])
    #             edges.pop(i)
    #         else:
    #             visited.add(edges[i][0])
    #             visited.add(edges[i][1])
    #             edges.pop(i)
    #         i = 0
    #     else:
    #         i += 1
    # return dup[-1]
    visited = set([edges[0][0], edges[0][1]])
    edges.pop(0)
    dup = []
    for x in edges:
        if x[0] in visited or x[1] in visited:
            if x[0] in visited and x[1] in visited:
                dup.append(x)
            else:
                visited.add(x[0])
                visited.add(x[1])
        else:
            edges.append(x)
    return dup[-1]

a = [[1,5],[3,4],[3,5],[4,5],[2,4]]
findRedundantConnection(a)