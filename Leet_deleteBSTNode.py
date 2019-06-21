class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deleteNode(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    if root:
        if root.val < key:
            root.right = deleteNode(root.right, key)
        elif root.val > key:
            root.left = deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = root.left
                mx = temp.val
                while temp.right:
                    temp = temp.right
                    mx = temp.val
                root.val = temp.val
                root.left = deleteNode(root.left, mx)
        return root

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.left.right = TreeNode(2.5)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(4.5)
root.right.right = TreeNode(7)

deleteNode(root, 3)


