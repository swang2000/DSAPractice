import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findFrequentTreeSum(root):
    out = collections.Counter()

    def inOrder(root):
        if not root:
            return 0
        else:
            s = root.val + inOrder(root.left) + inOrder(root.right)
            out[s] += 1
            return s
    inOrder(root)
    mx = max([v for k, v in out.most_common()])

    return [k for k, v in out.most_common() if v== mx]


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
findFrequentTreeSum(root)
