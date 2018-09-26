"""
A tree is a frequently-used data structure to simulate a hierarchical tree structure.

Each node of the tree will have a root value and a list of references to other nodes which
are called child nodes. From graph view, a tree can also be defined as a directed acyclic graph
which has N nodes and N-1 vertices.

A Binary Tree is one of the most typical tree structure. As the name suggests, a binary tree is
a tree data structure in which each node has at most two children, which are referred to as the
left child and the right child.

dfs
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
    1
   /  \
  4    2
 /\   / \
 5 6 3  7

树的前中后序遍历

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursively preorder 先序遍历的顺序如下（根、左、右） [1,4,5,6,2,3,7]
def preorderTraversal1(root):
    res = []
    dfs(root, res)
    return res


def dfs(root, res):
    if root:
        res.append(root.val)
        dfs(root.left, res)
        dfs(root.right, res)


# iteratively
def preorderTraversal(root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res


# inorder 中序遍历的顺序如下（左、根、右）[5,4,6,1,3,2,7]
def inorder(root):
    res = []
    dfs2(root, res)
    return res


def dfs2(root, res):
    if root:
        dfs2(root.left, res)
        res.append(root.val)
        dfs2(root.right, res)


# postorder 后序遍历 使用后续遍历的顺序如下（左、右、根） [5,6,4,3,7,2,1]
def postorder(root):
    res = []
    dfs3(root, res)
    return res


def dfs3(root, res):
    if root:
        dfs3(root.left, res)
        dfs3(root.right, res)
        res.append(root.val)


root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
print(inorder(root))
