"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an

"""


class Solution(object):
    # 牛顿法
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return int(r)

    # 二分法
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        low, high = 1, x
        while low <= high:
            mid = (high + low) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = int(high - 1)
            else:
                low = int(low + 1)
        if high * high < x:
            return int(high)
        else:
            return int(low)


test = Solution()
print(test.mySqrt2(37))
