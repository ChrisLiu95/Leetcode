"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

"""

import bisect


class Solution(object):
    def increasingTriplet(self, nums):
        temp = [float("inf"), float("inf")]
        try:
            for num in nums:
                temp[bisect.bisect_left(temp, num)] = num
            return False

        except IndexError:
            return True

    def increasingTriplet2(self, nums):
        first, second = float("inf"), float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    # [3,4, 1,6]
    # first:1  second:4


test = Solution()
print(test.increasingTriplet2([5, 4, 3, 2, 1]))
