"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        if root:
            if root.val == val:
                return root
            elif root.val < val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)

    def searchBST2(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root and root.val != val:
            root = root.left if root.val > val else root.right
        return root
