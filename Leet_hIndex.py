def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, v in enumerate(citations):
        if v > i: h += 1
    return h


citations = [3,0,6,1,5]
hIndex(citations)
