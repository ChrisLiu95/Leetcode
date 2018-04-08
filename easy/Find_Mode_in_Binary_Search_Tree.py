"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

"""


# naive solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [root]
        mydir = {}
        res = []
        while stack:
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                mydir[node.val] = mydir.get(node.val, 0) + 1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        freq = max(mydir.values())
        for node, fre in mydir.items():
            if fre == freq:
                res.append(node)
        return res
