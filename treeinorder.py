'''
Inorder Tree Traversal without Recursion
Using Stack is the obvious way to traverse tree without recursion. Below is an algorithm for traversing binary tree
using stack. See this for step wise step execution of the algorithm.

1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.

'''

import CdataS.BT.BianrySearchTree as tree

def inortreeworecur(root):
    stack = []

    while True :
        while root:
            stack.append(root)
            root = root.left_child
        root = stack.pop()
        print(root.value, end='>> ')
        root = root.right_child
        if root is None and (len(stack)==0):
            break





bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
inortreeworecur(bst.root)







