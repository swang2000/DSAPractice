class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None: return []
    q = [[root]]
    for level in q:
        record = []
        for node in level:
            if node.left: record.append(node.left)
            if node.right: record.append(node.right)
        if record: q.append(record)
    return [[x.val for x in level] for level in q]


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right = TreeNode(7)

levelOrder(t)


