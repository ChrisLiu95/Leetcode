"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.


!! 经典中序traversal， BST 中序 必须为 递增
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        res = []
        self.dfs(root, res)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)


# search value in a binary search tree
def find(root, value):
    """
    :param root: TreeNode
    :param value: int
    :return: boolean
    """
    while root:
        if root.val == value:
            return True
        elif root.val > value:
            root = root.left
        else:
            root = root.right
    return False
