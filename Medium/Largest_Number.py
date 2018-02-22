"""

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Sort函数是list列表中的函数，而sorted可以对list或者iterator进行排序。

"""

from functools import cmp_to_key


class Solution(object):
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]  # this is a list
        # nums = map(str, nums) this is iterator
        nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1 if x + y < y + x else 0), reverse=True)
        return str(int(''.join(nums)))


test = Solution()
print(test.largestNumber([3, 30, 34, 5, 9]))
