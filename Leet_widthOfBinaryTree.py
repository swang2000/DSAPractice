class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def widthOfBinaryTree(root):
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)

    return ans


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

widthOfBinaryTree(root)

