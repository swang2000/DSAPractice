
def scoreOfParentheses(S):
    ans = bal = 0
    for i, x in enumerate(S):
        if x == '(':
            bal += 1
        else:
            bal -= 1
            if S[i - 1] == '(':
                ans += 1 << bal
    return ans


s = "(()(()))"
scoreOfParentheses(s)
