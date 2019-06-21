#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def subtreeWithAllDeepest(root):
    def depth(root, d):
        if not root:
            return (d, None)
        l, r = depth(root.left, d + 1), depth(root.right, d + 1)
        if l[0] > r[0]: return (l[0], l[1])
        elif l[0] < r[0]: return (r[0], r[1])
        else:
            return l[0], root.val
    return depth(root, 0)[1]


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

subtreeWithAllDeepest(root)




