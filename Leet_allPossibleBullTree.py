# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def allPossibleFBT(N):
    if N % 2 == 0: return [] # the number of node must be odd
    cache = {}
    for i in range(1,N+1,2): # only consider odd number
        if i == 1:  # initialize
            cache[1] = [TreeNode(0)]
            continue
        cache[i] = []
        for j in range(1,i,2): # j represent the number of node in left child
            for lkid in cache[j]:
                for rkid in cache[i-1-j]:
                    node = TreeNode(0)
                    node.left = lkid
                    node.right = rkid
                    cache[i].append(node)
    return cache[N]


allPossibleFBT(7)