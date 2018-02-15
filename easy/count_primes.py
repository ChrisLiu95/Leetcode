"""
Description:

Count the number of prime numbers less than a non-negative number, n.

"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [True] * n
        res[0], res[1] = False, False
        for i in range(2, n):
            if res[i]:
                for j in range(i, (n - 1) // i + 1):
                    res[i * j] = False
        return sum(res)


test = Solution()
print(test.countPrimes(5))
