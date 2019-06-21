def wordBreak(s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(s[j:i] in words for j in range(i) if ok[j]),
    return ok[-1]



s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
wordBreak(s, wordDict)