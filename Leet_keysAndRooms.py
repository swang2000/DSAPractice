def canVisitAllRooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    visited = [False] * len(rooms)
    keys = [False] * len(rooms)
    keys[0] = True

    def dfs(i):
        if visited[i]:
            return
        visited[i] = True
        for keylist in rooms[i]:
            keys[keylist] = True
            dfs(keylist)

    dfs(0)
    if len(rooms) == 1: return True
    if sum(keys) == len(rooms):
        return True
    else:
        return False



a = [[1,3],[3,0,1],[2],[0]]
canVisitAllRooms(a)
