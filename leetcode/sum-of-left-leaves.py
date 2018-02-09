# sum of left leaves
# find the sum of left leaves of a given binary tree
""""
    3
   / \
   9 20
     /|
    15 7

return 9+15 = 24

"""

class Solution():

    def sum_of_left_leaves(self, root):

        self.count = 0

        def tranverse(tree, isLeftChild):
            if not tree:
                return
            tranverse(tree.left, True)

            if isLeftChild:
                if not left.root and if not right.root:
                    self.count += root.val

            tranverse(tree.right, False)
        tranverse(root,False)

        return self.count
