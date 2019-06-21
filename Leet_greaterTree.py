class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def convertBST(root):
    def reverse(root, v):
        if root:
            r, l = reverse(root.right)[1], reverse(root.left)[1]
            root.val = root.val + r
            root.left = reverse(root.left)[0]
            root.right =  reverse(root.right)[0]
            return [newnode, root.val + r]
        else:
            return [None, 0]
    return reverse(root)[0]


root = TreeNode(2)
root.left = TreeNode(0)
root.right = TreeNode(3)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(1)


r = convertBST(root)
