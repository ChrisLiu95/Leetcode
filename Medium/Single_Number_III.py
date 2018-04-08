"""
Given an array of numbers nums, in which exactly two elements appear only once and all the
other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant
space complexity?

"""


class Solution(object):
    # time: O(n) space:O(n)
    def singleNumber(self, nums):
        dir = {}
        for num in nums:
            dir[num] = dir.get(num, 0) + 1
        res = []
        for key, val in dir.items():
            if val % 2 == 1:
                res.append(key)
        return res

    # best answer
    def singleNumber2(self, nums):
        res = 0
        res1 = 0
        res2 = 0

        for num in nums:
            res ^= num

        mask = 1

        while res & mask == 0:
            mask = mask << 1

        for num in nums:
            if num & mask:
                res1 ^= num
            else:
                res2 ^= num

        return [res1, res2]

    # slow
    def singleNumber3(self, nums):
        res = 0
        res1 = 0
        res2 = 0

        for num in nums:
            res ^= num

        temp = res
        digit = 0
        while temp & 1 != 1:
            temp = temp >> 1
            digit += 1

        def isdigit(number):
            for i in range(digit):
                number = number >> 1
            return number & 1 == 1

        for num in nums:
            if isdigit(num):
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]
