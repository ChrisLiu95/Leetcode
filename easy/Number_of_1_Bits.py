"""
Write a function that takes an unsigned integer and returns the number of ’1' bits
 it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.

"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        oribin = '{0:032b}'.format(n)
        count = 0
        for i in oribin:
            if i == '1':
                count += 1
        return count

    def hammingWeight2(self, n):
        return bin(n).count('1')


test = Solution()
print(test.hammingWeight2(11))
