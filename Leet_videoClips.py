def videoStitching(clips, T):
    end, end2, res = -1, 0, 0
    for i, j in sorted(clips):
        if end2 >= T or i > end2:
            break
        elif end < i <= end2:
            res, end = res + 1, end2
        end2 = max(end2, j)
    return res if end2 >= T else -1

clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
T = 9
videoStitching(clips, T)
