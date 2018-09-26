"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

中序遍历即可，BST中序遍历为递增，否则不是BST
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def ifBST(self, root):
        res = []
        self.dfs(root, res)
        print(res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)


pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

test = Solution()
print(test.ifBST(pNode1))
