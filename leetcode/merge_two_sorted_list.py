"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing
together the nodes of the first two lists.

"""


class Solution(object):

    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1+l2
        elif l1[0] < l2[0]:
            return [l1[0]] + (self.merge(l1[1:], l2))
        else:
            return [l2[0]] + (self.merge(l1, l2[1:]))

    def merge2(self, l1, l2):
        new = []
        while l1 and l2:
            if l1[0] < l2[0]:
                new += [l1[0]]
                l1 = l1[1:]
            else:
                new += [l2[0]]
                l2 = l2[1:]
        if l1:
            return new + l1
        return new + l2


test = Solution()
print(test.merge([1, 3, 5], [2, 4, 6]))
print(test.merge2([1, 3, 4], [2, 9]))





