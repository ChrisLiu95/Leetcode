"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        res = []
        self.dfs(root, res, [], sum)
        return res

    def dfs(self, node, res, path, sum):
        if not node:
            return
        if node.val == sum and not node.left and not node.right:
            res.append(path + [node.val])
            return
        self.dfs(node.left, res, path + [node.val], sum - node.val)
        self.dfs(node.right, res, path + [node.val], sum - node.val)
