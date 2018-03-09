"""
Given a Binary Search Tree and a target number, return true if there exist two elements
in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def two_sum_IV(self, root, k):
        dfs, seen = [root], set()

        for node in dfs:
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left:
                dfs.append(node.left)
            if node.right:
                dfs.append(node.right)
        return False
