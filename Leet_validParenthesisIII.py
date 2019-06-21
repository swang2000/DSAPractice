import collections

def checkValidString(s):

    stack = []
    for c in s:
        if c in ('(', '*'):
            stack.append(c)
        else:
            if len(stack) == 0: return False
            i = len(stack) - 1
            while i >= 0 and stack[i] != '(':
                i -= 1
            stack = stack[:i] + stack[i + 1:]
    m = collections.Counter(stack)
    if len(stack) >0 and m.get('*', 0)==0: return False
    elif m.get('*', 0) >= m.get(')', 0)   or (m.get('*', 0) >= m.get('(', 0)):
        return True
    else:
        return False

s = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"

checkValidString(s)
