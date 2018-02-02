import CdataS.BT.BianrySearchTree as tree
def distofnode(a, x):
    if a != None:
        if a.value == x:
            return 0
        else:
            ld = distofnode(a.left_child, x)
            rd = distofnode(a.right_child, x)
            if ld != None:
                return ld + 1
            elif rd != None:
                return rd + 1





bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
bst.insert(2.7)
distofnode(bst.root, 2.7)

