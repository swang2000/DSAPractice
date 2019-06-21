import collections
def findItinerary(tickets):
    # fmap = collections.defaultdict(list)
    # for s, d in tickets:
    #     fmap[s].append(d)
    # out = ['JFK']
    #
    # key = 'JFK'
    # while key and len(fmap) >0:
    #     ds = fmap.pop(key, None)
    #     if ds:
    #         ds.sort()
    #         temp = ds.pop(0)
    #         out.append(temp)
    #         if ds:
    #             fmap[key] = ds
    #             oldkey = key
    #         key = temp
    #     elif fmap.get(oldkey, None):
    #         del out[-1]
    #         key = oldkey
    # return out


    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
    return route[::-1]

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
findItinerary(tickets)
