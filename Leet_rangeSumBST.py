# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:

    def rangeSumBST(self, root, L, R):
        def traverse(self, root, L, R):
            if root:
                if root.val >= L and root.val <= R:
                    self.nums += root.val
                if root.val > L:
                    traverse(self, root.left,L, R)

                if root.val < R:
                    traverse(self, root.right, L, R)
        self.nums = 0
        traverse(self, root, L, R)
        return self.nums



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

s = Solution()
s.rangeSumBST(root, 7, 15)

