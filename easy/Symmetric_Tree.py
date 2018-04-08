"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        if not q and not q:
            return True
        if not q or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.dfs(p.left, q.right) and self.dfs(p.right, q.left)
