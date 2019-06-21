class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def sortedArrayToBST(nums):
    if len(nums)==0: return None
    root = TreeNode(nums[len(nums) // 2])
    root.left = sortedArrayToBST(nums[:len(nums) // 2])
    root.right = sortedArrayToBST(nums[len(nums) // 2 + 1:])
    return root

a = [-10,-3,0,5,9]
root = sortedArrayToBST(a)
