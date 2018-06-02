"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 比较每一个node的左右最大树深相差是否超过1
        def balance(root):
            if not root:
                return [True, -1]
            left = balance(root.left)
            right = balance(root.right)
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [isBalanced, max(left[1], right[1]) + 1]

        return balance(root)[0]
