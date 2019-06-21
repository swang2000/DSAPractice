
from itertools import accumulate
def leastBricks(wall):

    asum =[list(accumulate(row)) for row in wall]
    nums = {}
    for row in asum:
        for x in row:
            nums[x] = nums.get(x, 0) +1
    a = sorted(nums.values(), reverse= True)
    return len(wall) -a[1]


wall =  [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

leastBricks(wall)
