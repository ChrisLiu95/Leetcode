"""
find the number of 1 in a binary number

"""


class Solution(object):
    # O(n)
    def findN(self, n):
        res = 0
        while n != 0:
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res

    # O(n) n is the number if 1
    def findN2(self, n):
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res


test = Solution()
print(test.findN2(4))
