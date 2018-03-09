"""
given by numbers of coin of 1 and 5, determine
whether some or all of them can sum up to a given target.

"""


class Solution(object):
    def coin_to_target(self, num1, num5, target):
        j = 0
        while j <= num5 and j * 5 <= target:
            if target - j * 5 <= num1:
                return True
            j += 1
        return False


test = Solution()
print(test.coin_to_target(1, 2, 10))
