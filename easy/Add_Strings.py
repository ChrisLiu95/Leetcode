"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = list(num1)
        l2 = list(num2)

        n1 = 0
        n2 = 0

        for char in l1:
            n1 = n1 * 10 + int(char)
        for char in l2:
            n2 = n2 * 10 + int(char)

        return str(n1 + n2)
