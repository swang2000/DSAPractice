# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if len(nums) > 0:
            a = max(nums)
            root = TreeNode(a)
            root.left = self.constructMaximumBinaryTree(nums[:nums.index(a)])
            root.right = self.constructMaximumBinaryTree(nums[nums.index(a) + 1:])
            return root


nums = [3,2,1,6,0,5]
t = Solution()
t.constructMaximumBinaryTree(nums)
