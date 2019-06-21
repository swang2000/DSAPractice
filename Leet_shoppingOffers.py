def shoppingOffers(price, special, needs):
    d = {}

    def dfs(cur):
        val = sum(cur[i] * price[i] for i in range(len(needs)))  # cost without special
        for spec in special:
            tmp = [cur[j] - spec[j] for j in range(len(needs))]
            if min(tmp) >= 0:  # skip deals that exceed needs
                val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1])  # .get check the dictionary first for result, otherwise perform dfs.
        d[tuple(cur)] = val
        return val

    return dfs(needs)

price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]

shoppingOffers(price, special, needs)