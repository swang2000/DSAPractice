# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d > 2:
            self.addOneRow(root.left, v, d - 1)
            self.addOneRow(root.right, v, d - 1)
            return root
        if d == 2:
            l, r = root.left, root.right
            root.left, root.right = TreeNode(v), TreeNode(v)
            root.left.left, root.right.right = l, r
            return root

        elif d == 1:
            head = TreeNode(v)
            head.left = root
            return head


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

t = Solution()
t.addOneRow(root, 1, 2)

