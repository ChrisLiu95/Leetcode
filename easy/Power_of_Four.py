"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.


bin(4)
'0b100'
bin(16)
'0b10000'
bin(64)
'0b1000000'
"""


class Solution(object):
    def isPowerOfFour(self, num):
        return num > 0 and num & (num - 1) == 0 and len(bin(num)[3:]) % 2 == 0
