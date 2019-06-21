def validateStackSequences(pushed, popped):
    n = len(pushed)
    st = []
    while popped:
        while (st and st[-1] != popped[0]) and pushed or not st:
            st.append(pushed.pop(0))
        if st[-1] != popped[0]: return False
        else:
            st.pop()
            popped.pop(0)
    return True if len(st) == 0 else False



pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]

validateStackSequences(pushed, popped)


