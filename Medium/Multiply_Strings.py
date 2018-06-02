"""

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        carry1 = 1
        for n1 in num1[::-1]:
            carry2 = 1
            for n2 in num2[::-1]:
                res += int(n1) * int(n2) * carry1 * carry2
                carry2 *= 10
            carry1 *= 10
        return str(res)
