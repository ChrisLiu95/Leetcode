"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        res = 0

        while queue:
            tempq = []

            for node in queue:
                if node.left:
                    tempq.append(node.left)
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                if node.right:
                    tempq.append(node.right)

            queue = tempq
        return res
