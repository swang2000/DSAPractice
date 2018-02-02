'''
Preorder to Postorder
Show Topic Tags           Amazon
Given an array representing preorder traversal of BST, print its postorder traversal.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[i].

Output:
Postorder traversal of the given preorder traversal is printed. Otherwise 'NO' is printed.

Constraints:
1 <=T<= 100
1 <= N <= 1000
1 <= arr[i] <= 1000

Example:

Input:
3
5
40 30 35 80 100
8
40 30 32 35 80 90 100 120
8
7  9 6 1 4 2 3 40

Output:
35 30 100 80 40
35 32 30 120 100 90 80 40
NO

** For More Input/Output Examples Use 'Expected Output' option **
'''


# def pretopost(a):
#     s = []
#     temps = []
#     out = []
#     key = -2**31
#     for value in a:
#         while len(s) >0 and (value > s[-1]):
#             key = s.pop(-1)
#         s.append(value)
#         while len(temps) >0 and temps[-1] < key:
#             out.append(temps.pop(-1))
#         temps.append(value)
#     while len(temps) >0:
#         out.append(temps.pop(-1))
#
#
#
#
# a = [40, 30, 25, 28, 32, 35, 80, 90, 100, 120]
# pretopost(a)


'''
Count number of ways to reach destination in a Maze
3
Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell.
A cell in given maze has value -1 if it is a blockage or dead end, else 0.

From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.
'''
###  recursive method

# import numpy as np
# def countpaths(maze):
#     m, n = maze.shape
#     # m -= 1
#     # n -= 1
#     if m==1 and (n==1):
#         return 0
#     elif m ==1 and sum(maze[m-1,0:n])>=0:
#         return 1
#     elif n ==1 and sum(maze[0:m,n-1])>=0:
#         return 1
#     elif m*n >0 and (maze[m-1,n-1] ==-1):
#         return 0
#     elif (m*n >0) and (maze[m-1,n-1]!= -1):
#         return countpaths(maze[0:m-1,0:n]) + countpaths(maze[0:m, 0:n-1])
#     else:
#         return 0
#
#
#
# maze = np.array([[0,  0, 0, 0],
#               [0, -1, 0, 0],
#               [-1, 0, 0, 0],
#               [0,  0, 0, 0]])
# countpaths(maze)


### Dynamic programming
# import numpy as np
# def countpaths2(maze):
#     if maze[0,0] == -1:
#         return 0
#     m, n = maze.shape
#     for i in range(m):
#         if maze[i, 0] ==0:
#             maze[i, 0] =1
#         else:
#             break
#     for j in range(n):
#         if maze[0, j] >=0:
#             maze[0, j] =1
#         else:
#             break
#
#     for i in range(1, m):
#         for j in range(1,n):
#             if maze[i, j] != -1:
#                 if maze[i-1, j] >0:
#                     maze[i, j] = maze[i, j] + maze[i-1, j]
#                 if maze[i, j-1] > 0:
#                     maze[i, j] = maze[i, j] + maze[i, j-1]
#     return maze
#
# maze = np.array([[0,  0, 0, 0],
#               [0, -1, 0, 0],
#               [-1, 0, 0, 0],
#               [0,  0, 0, 0]])
# countpaths2(maze)
#

'''
Dynamic Programming | Set 10 ( 0-1 Knapsack Problem)
3.3
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum
value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an
item, either pick the complete item, or don’t pick it (0-1 property).
'''

# Recursive solution
def knapsack(v, w, k):
    if len(w)==0 or (k<=0):
        return 0
    if w[0] > k:
        return knapsack(v[1:], w[1:], k)
    return max(v[0]+knapsack(v[1:], w[1:], k-w[0]), knapsack(v[1:], w[1:], k))

v = [60, 100, 120]
w = [10, 20, 30]
knapsack(v, w, 50)


# Dynamaic programming

#def knapsack2(v, w, k):



'''

Print Ancestors of a given node in Binary Tree
2.5
Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.

For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.


              1
            /   \
          2      3
        /  \
      4     5
     /
    7
'''
import CdataS.BT.BianrySearchTree as tree
def ancestors(a, k):
    if a != None:
        if a.value == k:
            return True
        else:
            if a.left_child and (ancestors(a.left_child, k)):
                print(a.value)
                return True
            elif a.right_child and (ancestors(a.right_child, k)):
                print(a.value)
                return True


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
ancestors(bst.root, 2)


'''
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL).
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
The order of nodes in DLL must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
'''

import CdataS.BT.BianrySearchTree as tree
def fixprevpt(root, prev):
    if root != None:
        fixprevpt(root.left_child, prev)
        root.left_child = prev[0]
        prev[0] = root
        fixprevpt(root.right_child, prev)
        return root

def fixnextpt(root, next):
    while root.right_child:
        root = root.right_child
    while root and root.left_child:
        next= root
        root = root.left_child
        root.right_child = next

    return root


def printDLL(a):
    while a:
        print(a.value)
        a = a.right_child


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)

prev = [None]
next = None
fixprevpt(bst.root, prev)
a = fixnextpt(bst.root, next)
printDLL(a)

'''
Foldable Binary Trees
2.6
Question: Given a binary tree, find out if the tree can be folded or not.

A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. An empty tree is considered as foldable.

Consider the below trees:
(a) and (b) can be folded.
(c) and (d) cannot be folded.
'''

import CdataS.BT.BianrySearchTree as tree
def checkroot(a):
    if a!= None:
        if a.left_child and a.right_child:
            return checkmirror(a.left_child, a.right_child)
        elif a.left_child == None and (a.right_child == None):
            return True
        else:
            return False

def checkmirror(a, b):
    if a.left_child and (a.right_child) and (b.left_child and (b.right_child)):
        return checkmirror(a.left_child, b.right_child) and checkmirror(a.right_child, b.left_child)
    elif a.left_child and (b.right_child) and (a.right_child == None and (b.left_child == None)):
        return checkmirror(a.left_child, b.right_child)
    elif a.right_child and (b.left_child) and (a.left_child == None and (b.right_child == None)):
        return checkmirror(a.right_child, b.left_child)
    elif a.right_child == None and (a.left_child == None) and (b.left_child == None and (b.right_child == None)):
        return True
    else:
        return False



bst = tree.BST()
bst.insert(10)
bst.insert(7)
bst.insert(6)
bst.insert(11)
bst.insert(10.5)
checkroot(bst.root)



import CdataS.BT.BianrySearchTree as tree
def counthalfnodes(a, n):
    if a != None:
        if a.left_child and (a.right_child == None):
            n[0] += 1
            counthalfnodes(a.left_child, n)
        elif a.right_child and (a.left_child == None):
            n[0] += 1
            counthalfnodes(a.right_child, n)
        elif a.left_child and a.right_child:
            counthalfnodes(a.left_child, n)
            counthalfnodes(a.right_child, n)

bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
num = [0]
counthalfnodes(bst.root, num)


'''
Merge Two Binary Trees by doing Node Sum (Recursive and Iterative)
2.5
Given two binary trees. We need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then
sum node values up as the new value of the merged node. Otherwise, the non-null node will be used as the node of new tree.

Example:

Input:
     Tree 1            Tree 2
       2                 3
      / \               / \
     1   4             6   1
    /                   \   \
   5                     2   7

Output: Merged tree:
         5
        / \
       7   5
      / \   \
     5   2   7
Note: The merging process must start from the root nodes of both trees.
'''


import CdataS.BT.BianrySearchTree as tree

def mergetree(a, b):
    if a== None and b == None:
        return
    elif a and b:
        out = tree.Node(a.value + b.value)
        out.left_child = mergetree(a.left_child, b.left_child)
        out.right_child = mergetree(a.right_child, b.right_child)
    elif b:
        out = tree.Node(b.value)
        out.left_child = mergetree(None, b.left_child)
        out.right_child = mergetree(None, b.right_child)
    elif a:
        out = tree.Node(a.value)
        out.left_child = mergetree(a.left_child, None)
        out.right_child = mergetree(a.right_child, None)
    return out



bst1 = tree.BST()
bst2 = tree.BST()
bst1.insert(4)
bst1.insert(2)
bst1.insert(1)
bst1.insert(5)

bst2.insert(3)
bst2.insert(1)
bst2.insert(2)
bst2.insert(6)
bst2.insert(7)
c = bst1
mergetree(bst1.root, bst2.root)


'''
Find distance from root to given node in a binary tree
2.4
Given root of a binary tree and a key x in it, find distance of the given key from root. Distance means num­ber of
edges between two nodes.

Examples:

Input : x = 45,
        Root of below tree
        5
      /    \
    10      15
    / \    /  \
  20  25  30   35
       \
       45
Output : Distance = 3
There are three edges on path
from root to 45.

For more understanding of question,
in above tree distance of 35 is two
and distance of 10 is 1.
'''

import CdataS.BT.BianrySearchTree as tree
def distofnode(a, x):
    if a != None:
        if a.value == x:
            return 0
        else:
            ld = distofnode(a.left_child, x)
            rd = distofnode(a.right_child, x)
            if ld != None:
                return ld+1
            elif rd != None:
                return rd +1


bst = tree.BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(2.5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
distofnode(bst.root, 2.5)




'''
Dynamic Programming | Set 3 (Longest Increasing Subsequence)
3.1
We have discussed Overlapping Subproblems and Optimal Substructure properties.

Let us discuss Longest Increasing Subsequence (LIS) problem as an example problem that can be solved using Dynamic
Programming.
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

'''



def findLIS(a):
    n = len(a)
    length = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if a[i] > a[j] and (length[j]+1 >length[i]):
                length[i] = length[j] + 1
    return length[n-1]

a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
findLIS(a)

'''
Dynamic Programming | Set 4 (Longest Common Subsequence)
2.8
We have discussed Overlapping Subproblems and Optimal Substructure properties in Set 1 and Set 2 respectively.
We also discussed one example problem in Set 3. Let us discuss Longest Common Subsequence (LCS) problem as one more
example problem that can be solved using Dynamic Programming.

LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example,
“abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different
possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences
between two files), and has applications in bioinformatics.
'''

import numpy as np
def findLCS(a, b):
    m = len(a)
    n = len(b)
    LCS = np.zeros((m+1,n+1))
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                LCS[i, j] = LCS[i-1, j-1] +1
            else:
                LCS[i, j] = max(LCS[i, j-1], LCS[i-1, j])
    return LCS


a = 'AGGTAB'
b = 'GXTXAYB'
findLCS(a,b)



