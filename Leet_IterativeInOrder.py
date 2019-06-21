
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




def inorderTraversal(root):
    s = [(False, root)]
    res = []
    if not root: return []
    while len(s)>0:
        flag, v = s.pop()
        if v:
            if not flag:
                s.append((False, v.right))
                s.append((True, v))
                s.append((False, v.left))
            else:
                res.append(v.val)
    return res

t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

inorderTraversal(t)
