"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        res, i, start = [], 0, 0
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i + 1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i + 1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
        return res

    def printRange(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)


test = Solution()
print(test.summaryRanges([0, 1, 2, 4, 5, 7]))
