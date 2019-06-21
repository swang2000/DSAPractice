def ihist(nums):
    '''
    Generate an integer histogram from a list of integers 'nums'.
    The histogram is a dictionary mapping integers to their counts.
    Print the resulting histogram and return it.
    '''
    hist = {}
    for n in nums:
        if not (n in hist):
            hist[n] = 1
        else:
            hist[n] += 1

    # print contents of histogram dictionary 'hist'
    # print('{', end='')
    # for num, count in enumerate(hist):
    #     if num < len(hist)-1:
    #         print('{}: {}'.format(count, hist[count]), end=', ')
    #     else:
    #         print('{}: {}'.format(count, hist[count]), end='')
    # print('}')

    return hist


def test_ihist():
    #assert ihist([]) == {}
    assert ihist([1]) == {1: 1}
    assert ihist([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
    assert ihist([1, 1, 1]) == {1: 3}
    assert ihist([1, 2, 3, 4, 2, 3, 4, 3, 4, 4]) == \
           {1: 1, 2: 2, 3: 3, 4: 4}
    assert ihist([1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 4, 1]) == \
           {1: 2, 2: 2, 3: 3, 4: 4, 5: 3, 6: 1}


test_ihist()
#ihist([1])