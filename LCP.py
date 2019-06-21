def longestCommonPrefix(strs) -> str:
    comm = strs[0]
    for i in range(1, len(strs)):
        for j in range(len(comm)):
            if j == 0 and comm[j] != strs[i][j]:
                return ''
            elif (j<len(strs[i])) and comm[j] == strs[i][j]:
                continue
            else:
                comm = comm[:j]
                break
    return comm

strs = ["flow","flower","flowersed"]
longestCommonPrefix(strs)