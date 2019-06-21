# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        out = []

        def preOrder(root):
            if root:
                out.append(root.val)
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        return ' '.join(map(str, out))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = list(map(int, data.split()))

        def build(mn, mx):
            if vals and mn < vals[0] < mx:
                root = TreeNode(vals.pop(0))
                root.left = build(mn, root.val)
                root.right = build(root.val, mx)
                return root
            return None

        return build(float('-infinity'), float('infinity'))

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(8)

a = Codec()
b = a.serialize(root)
print(b)
c = a.deserialize(b)
