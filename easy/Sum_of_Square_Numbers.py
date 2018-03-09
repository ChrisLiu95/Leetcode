"""
Given a non-negative integer c, your task is to decide whether there're two integers a
and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False

"""
import math


class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            temp = left ** 2 + right ** 2
            if temp == c:
                return True
            elif temp < c:
                left += 1
            else:
                right -= 1
        return False


test = Solution()
print(test.judgeSquareSum(2))
