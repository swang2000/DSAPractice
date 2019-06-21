import collections

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    out = []
    in_degrees = collections.defaultdict(int)
    courses = collections.defaultdict(list)
    for u, v in prerequisites:
        courses[v].append(u)
        in_degrees[u] += 1
        in_degrees[v] += 0
    start = [u for u, v in in_degrees.items() if v == 0]
    while start:
        k = start.pop(0)
        out.append(k)
        for i in courses[k]:
            in_degrees[i] -= 1

            if in_degrees[i] == 0:
                start.append(i)
    for u in in_degrees:  # if graph has edge
        if in_degrees[u]:
            return False
    return True



canFinish(2, [[1,0]])
