def nextGreaterElement(n):
    """
    :type n: int
    :rtype: int
    """

    st = []
    a = str(n)
    l = len(a)
    if a == ''.join(sorted(a, reverse=True)): return -1
    else:
        for i, v in enumerate(a[-1::-1]):
            if not st or st[-1] <= v:
                st.append(v)
            else:
                break
        bm = min([ x for x in st if x > v])
        st.remove(bm)
        st.append(a[l-i-1])
        s = ''.join(a[:l-i-1] + bm + ''.join(sorted(st)))
    return int(s)


nextGreaterElement(1999999999)