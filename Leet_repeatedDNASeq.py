# def findRepeatedDnaSequences(s):
    # n = len(s)
    # out = set()
    # for i in range(n - 10):
    #     for j in range(i+1, n-9):
    #         if s[i:(i+ 10)] == s[j:(j + 10)]:
    #             out.add(s[i:(i + 10)])
    #             break
    # return list(out)
def findRepeatedDnaSequences(s):
    r, record = set(), set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        [record, r][substring in record].add(substring)
    return list(r)

s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
# s= "AAAAAAAAAAA"
findRepeatedDnaSequences(s)