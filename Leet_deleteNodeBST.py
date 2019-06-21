class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deleteNode(root, key):
    if not root: return None
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left

        if root.left:
            # Find the right most leaf of the left sub-tree
            left_right_most, pre = root.left, root
            while left_right_most.right:
                left_right_most, pre = left_right_most.right, left_right_most

            # Attach right child to the right of that leaf
            left_right_most.left = root.left
            left_right_most.right = root.right
            pre.left = None
            # Return left child instead of root, a.k.a delete root
            return left_right_most




root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

deleteNode(root, 3)





