class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def constructFromPrePost(pre, post):
    if len(pre)==0: return None
    root = TreeNode(pre[0])
    if len(pre)==1: return root
    L = post.index(pre[1])+1
    root.left = constructFromPrePost(pre[1:L+1], post[:L])
    root.right = constructFromPrePost(pre[L+1:], post[L:-1])
    return root


pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

constructFromPrePost(pre,post)
