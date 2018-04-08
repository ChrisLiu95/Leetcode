"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        q = [root]
        level = 0

        while q:
            tmp = []
            nl = []
            level += 1

            for node in q:
                if node:
                    tmp.append(node.val)
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)
            q = nl
            if level % 2 is 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
        return res
