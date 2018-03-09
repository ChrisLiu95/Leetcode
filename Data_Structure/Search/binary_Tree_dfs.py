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
    \
     2
    /
   3
return [1,2,3].
"""


# recursively
def preorderTraversal1(self, root):
    res = []
    self.dfs(root, res)
    return res


def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)


# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
