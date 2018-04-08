"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear
twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

"""


class Solution(object):
    # space O(n)
    def findDuplicates(self, nums):
        dic = {}
        res = []

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for key, val in dic.items():
            if val == 2:
                res.append(key)
        return res

    def findDuplicates2(self, nums):
        # [4,3,2,7,8,2,3,1]
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res
