class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isCousins(root, x, y):
    sm = {}
    def depth(p, root, d):
        if root:
            sm[root.val] = (p, d)
            depth(root.val, root.left, d + 1)
            depth(root.val, root.right, d + 1)
        return

    depth(None, root, 0)
    return sm[x][1] == sm[y][1] and sm[x][0] != sm[y][0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

isCousins(root,4,5)


