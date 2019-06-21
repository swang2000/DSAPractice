def romanToInt(s: str) -> int:
    maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = maps[s[-1]]
    for i in range(len(s) - 1):
        if maps[s[i]] < maps[s[i + 1]]:
            num -= maps[s[i]]
        else:
            num += maps[s[i]]
    return num


romanToInt("MCMXCIV")