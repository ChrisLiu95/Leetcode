"""
print all prime number before n

"""


# 又是传说中的for else
class Solution(object):
    def prime(self, n):
        res = []
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                res.append(i)
        return res


test = Solution()
print(test.prime(30))
