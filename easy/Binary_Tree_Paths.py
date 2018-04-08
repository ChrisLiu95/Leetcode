"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # dfs
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, node, temp, res):
        if not node.left and not node.right:
            res.append(temp + str(node.val))
            return
        if node.left:
            self.dfs(node.left, temp + str(node.val) + "->", res)
        if node.right:
            self.dfs(node.right, temp + str(node.val) + "->", res)

    # bfs with stack
    def binaryTreePaths2(self, root):
        if not root:
            return []

        res, stack = [], [[root, ""]]

        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right:
                res.append(temp + str(node.val))
            if node.left:
                stack.append([node.left, temp + str(node.val) + "->"])
            if node.right:
                stack.append([node.right, temp + str(node.val) + "->"])
        return res


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
test = Solution()
print(test.binaryTreePaths2(root))
