"""
We define a harmonious array is an array where the difference between its maximum value and
its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence
among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

"""


class Solution(object):
    def Harmonious(self, nums):
        mydic = {}
        res = 0
        for i in nums:
            mydic[i] = mydic.get(i, 0) + 1
        for i in mydic:
            if mydic.get(i + 1, 0) > 0 and mydic[i] + mydic[i + 1] > res:
                res = mydic[i] + mydic[i + 1]
        return res


test = Solution()
print(test.Harmonious([1, 3, 2, 2, 5, 2, 3, 7]))
