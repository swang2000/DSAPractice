class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from functools import reduce
def isCompleteTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    out = [[root]]
    for node in out:

        j = []
        j.extend([root.left, root.right] for root in node if root)
        j = reduce(lambda x, y: x+y, j )
        if all([x == None for x in j]): return True
        if (None in j and None in node) or any([True for i in range(1, len(j)) if not j[i-1] and j[i]]): return False
        out.append(j)
    






root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

isCompleteTree(root)

