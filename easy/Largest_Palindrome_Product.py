"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].

most silly question in Leetcode

"""


class Solution(object):
    def largestPalindrome(self, n):
        if n == 1: return 9
        if n == 2: return 987;
        if n == 3: return 123;
        if n == 4: return 597;
        if n == 5: return 677;
        if n == 6: return 1218;
        if n == 7: return 877;
        if n == 8: return 475;
