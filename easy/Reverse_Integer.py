"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

"""


class Solution(object):
    def reverse(self, x):
        s = (x > 0) - (x < 0)   # python 3 判断一个数是否大于0
        r = int(str(x * s)[::-1])
        return s * r * (r < 2 ** 31)
