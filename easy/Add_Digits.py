"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = str(num)
        while len(res) != 1:
            res = str(sum(int(x) for x in str(res)))
        return int(res)

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num is 0:
            return 0
        else:
            temp = num % 9
            return 9 if temp is 0 else temp


test = Solution()
print(test.addDigits(38))
