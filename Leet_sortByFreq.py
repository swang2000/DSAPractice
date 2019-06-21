def frequencySort(s):
    fmap = {}
    for k in s:
        fmap[k] = fmap.get(k, 0) + 1
    orders = sorted(fmap.items(), key=lambda x: x[1], reverse=True)
    out = ''
    for k in orders:
        out += k[0] * k[1]

    return out

s = 'tree'
frequencySort(s)
