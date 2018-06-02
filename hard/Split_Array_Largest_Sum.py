"""
Given an array which consists of non-negative integers and an integer m, you can split the array into
m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # A ceiling is max sum allowed for each segment (sub-array).
        def isValidCeiling(nums, m, ceiling):
            count, total = 1, 0  # count - # of segments. total - temp sum of the current segment.
            for i in range(len(nums)):
                if total + nums[i] <= ceiling:
                    total += nums[i]  # add the number to the current segment.
                else:
                    total = nums[i]  # over the ceiling, start a new segment.
                    count += 1
                if count > m:
                    return False  # if need more segments than m, the this an invalid ceiling.
            return True  # if count <= m, then this is a valid ceiling, i.e. if we can split into less than M segments,
            # sure enough we can split into M segments.

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if isValidCeiling(nums, m, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
