
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def smallestFromLeaf(root):
    out = []

    def dfs(root, a):
        if root:

            dfs(root.left, a + chr(root.val + ord('a')))
            dfs(root.right, a + chr(root.val + ord('a')))
        else:
            out.append(a[-1::-1])

    dfs(root, '')
    return sorted(out)[0] if len(out) > 1 else sorted(out)[1]


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(1)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.right.left = TreeNode(0)

smallestFromLeaf(root)
[4,0,1,1]