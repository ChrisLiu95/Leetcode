"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

"""


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # LTE? wtf
        l = [str(i + 1) for i in range(n)]
        l = sorted(l)
        return map(int, l)

    def lexicalOrder2(self, n):
        list = [i + 1 for i in range(n)]
        # temp = sorted(list, key=lambda x: str(x))
        temp = sorted(list, key=str)

        return temp


test = Solution()
print(test.lexicalOrder2(20))
