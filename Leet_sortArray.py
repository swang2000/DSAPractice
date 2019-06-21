def sortArrayByParityII(A):
    odd, even = [], []
    for x in A:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    print(len(odd))
    return [x for xs in zip(even,odd) for x in xs]

A= [4,2,5,7]
sortArrayByParityII(A)