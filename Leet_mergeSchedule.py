def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort()
    out = [intervals[0]]

    for i in range(1, len(intervals)):
        if out[i - 1][1] <= intervals[i][0] <= intervals[i - 1][1]:
            out[i - 1] = [intervals[i - 1][0], max(out[i - 1][1], intervals[i][1])]
        else:
            out.append(intervals[i])
    return out



merge([[1, 3], [2, 6], [8, 10], [15, 18]])
