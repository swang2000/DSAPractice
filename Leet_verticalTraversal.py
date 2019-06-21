import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def verticalTraversal(root):
    pos = collections.defaultdict(list)

    def inorder(x, y, node):
        if node:
            pos[x].append((y, node.val))
            inorder(x - 1, y-1, node.left)
            inorder(x + 1, y-1, node.right)
        return
    inorder(0,0, root)
    y = sorted(pos.items(), key=lambda x: x[0])
    z = [x[1] for x in y]
    a = [sorted(i, key=lambda tup: tup[0], reverse=True) for i in z]

    return [[x[1] for x in item] for item in a]

t = TreeNode(0)
t.left = TreeNode(8)
t.right = TreeNode(1)
t.right.left = TreeNode(3)
t.right.right = TreeNode(2)
t.right.left.right = TreeNode(4)
t.right.right.left = TreeNode(5)
t.right.left.right.right = TreeNode(7)
t.right.right.left.left = TreeNode(6)
verticalTraversal(t)





