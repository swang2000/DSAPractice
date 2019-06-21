
import collections
def commonChars(A):
    res = collections.Counter(A[0])
    for a in A:
        res &= collections.Counter(a)
    return list(res.elements())

a = ["cool","lock","cook"]
commonChars(a)
