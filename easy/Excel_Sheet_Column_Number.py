"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""
import math


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        ans = 0
        for i in s:
            res.append(ord(i) - 64)
        for i in range(len(res)):
            ans += res[i] * (math.pow(26, len(res) - 1 - i))
        return ans

    def titleToNumber2(self, s):
        lenS = len(s)
        n2 = 0
        for i in range(0, lenS):
            n1 = ord(s[i]) - 64
            n2 = 26 * n2 + n1
        return n2


test = Solution()
print(test.titleToNumber2('AB'))
