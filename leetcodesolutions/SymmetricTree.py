#!/usr/bin/env python3
# SymmetricTree.py
# Author : Shipra

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    '''
    Given the root of a binary tree, check whether it is a
     mirror of itself (i.e., symmetric around its center).
    '''

    def isSymmetric(self, root: TreeNode):
        if root is None:
            return True

        if root.left == root.right:
            return  "equal"


element1 = TreeNode(1)
element2 = TreeNode(2)
element3 = TreeNode(2)
element4 = TreeNode(3)
element5 = TreeNode(4)
element6 = TreeNode(4)
element7 = TreeNode(3)

element1.left = element2
element1.right = element3
element2.left = element4
element2.right = element5
element3.left = element6
element3.right = element7

nums = [element1,element2,element3,element4,element5,element6,element7]

list = Solution()
list.isSymmetric(nums1)


