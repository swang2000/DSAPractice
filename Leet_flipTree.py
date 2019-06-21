class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 and root2:
            if root1.val == root2.val:
                if self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
                    return True
                return False
            return False
        elif (root1 and not root2):
            return False
        elif (root2 and not root1):
            return False

        return True



root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.left.left = TreeNode(4)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)
root1.right.left = TreeNode(6)


root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.left.right = TreeNode(6)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)



a = Solution()
a.flipEquiv(root1, root2)






