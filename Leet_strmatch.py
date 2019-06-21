def strStr(haystack, needle):
    a = len(haystack)
    b = len(needle)
    if b == 0:
        return 0
    if a == 0 or a < b:
        return -1
    i = j = 0
    while i < a-b:
        if haystack[i] == needle[0]:
            if haystack[i:i+b] == needle:
                return i
        i += 1
    return -1


strStr("mississippi", "issip")
