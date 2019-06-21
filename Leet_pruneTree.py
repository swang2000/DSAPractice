def pruneTree(root):
    def testP(root):
        if not root: return False
        l, r = testP(root.left), testP(root.right)
        if not l: root.left = None
        if not r: root.right = None
        return root.val == 1 or l or r

    return root if testP(root) else None

