# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left + right - 1
        dfs(root)
        return self.res


root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)

s = Solution()
s.distributeCoins(root)
