"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest
leaf node.

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # slow ugly dfs
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []

        res = []
        self.dfs(root, [], res)
        return min([len(x) for x in res])

    def dfs(self, node, temp, res):
        if not node.left and not node.right:
            res.append(temp + [node.val])
            return
        if node.left:
            self.dfs(node.left, temp + [node.val], res)
        if node.right:
            self.dfs(node.right, temp + [node.val], res)

    # bfs much faster bfs solution, beats 98% python solutions
    def minDepth2(self, root):
        if not root:
            return 0

        queue = [root]
        level = 0

        while queue:
            level += 1
            tempq = []
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)
            queue = tempq
        return level


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
test = Solution()
print(test.minDepth(root))
