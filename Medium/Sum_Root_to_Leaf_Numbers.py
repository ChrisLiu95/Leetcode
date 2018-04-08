"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0  # int is immutable 需要设为全局变量才能改变
        self.dfs(root, 0, self.res)
        return self.res

    def dfs(self, node, temp, res):
        if not node.left and not node.right:
            self.res += (temp * 10 + node.val)
            return
        if node.left:
            self.dfs(node.left, temp * 10 + node.val, res)
        if node.right:
            self.dfs(node.right, temp * 10 + node.val, res)
