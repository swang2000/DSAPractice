
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDiffInBST(root):
    treel = []

    def traverse(root):
        if not root:
            return
        else:
            if root.left:
                traverse(root.left)
            treel.append(root.val)
            if root.right:
                traverse(root.right)
    traverse(root)
    return min([a - b for a, b in zip(treel[1:], treel[:-1])])


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
minDiffInBST(root)


