"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""


class Solution(object):
    def maxproduct(self, nums):
        if not nums:
            return 0
        #  imax/imin stores the max/min product of subarray that ends with the current number A[i]
        res, cmax, cmin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger so we redefine
            # the extremums by swapping them
            if nums[i] < 0:
                cmax, cmin = cmin, cmax
            # // max/min product for the current number is either the current number itself
            # // or the max/min by the previous number times the current one
            cmax = max(cmax * nums[i], nums[i])
            cmin = min(cmin * nums[i], nums[i])

            res = max(res, cmax)
        return res


test = Solution()
print(test.maxproduct([2, 3, -2, 4]))
