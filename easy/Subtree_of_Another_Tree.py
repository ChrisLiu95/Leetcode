"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""


class Solution(object):
    def isSubTree(self, s, t):
        if not t:
            return True

        def sameTree(a, b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            elif a.val != b.val:
                return False
            else:
                return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        def dfs(a, b):
            if not a:
                return False
            if a.val == b.val and sameTree(a, b):
                return True
            return dfs(a.left, b) or dfs(a.right, b)

        return dfs(s, t)
