class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
def distanceK(root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    tmap = collections.defaultdict(list)
    out = []
    seen = set()
    def inOrder(root):
        if root:
            if root.left:
                tmap[root.val].append(root.left.val)
                tmap[root.left.val].append(root.val)
                inOrder(root.left)
            if root.right:
                tmap[root.val].append(root.right.val)
                tmap[root.right.val].append(root.val)
                inOrder(root.right)
    def dfs(target, k):
        if k ==0 and target: out.append(target)
        elif k >0 and target:
            seen.add(target)
            for x in tmap[target]:
                if x not in seen:
                    seen.add(x)
                    dfs(x, k-1)
    inOrder(root)
    dfs(target, K)
    return out

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

target = 5
K = 2
distanceK(root, target, K)