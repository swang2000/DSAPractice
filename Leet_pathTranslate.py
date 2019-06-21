def simplifyPath(path: str) -> str:
    ss = path.split('/')
    ss = [s for s in ss if s != '']
    stack = list()

    for str in ss:
        if str == '..':
            if len(stack) > 0:
                stack.pop()
        elif str == '.':
            pass
        else:
            stack.append(str)

    return '/' + '/'.join(stack)


simplifyPath("/a/../../b/../c//.//")