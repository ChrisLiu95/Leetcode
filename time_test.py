from time import time


class Solution(object):
    def timeTest(self):
        start = time()
        res = 0
        for i in range(1000000):
            if i & 1:
                res += 1
        end = time()
        return end - start


test = Solution()
print(test.timeTest())
