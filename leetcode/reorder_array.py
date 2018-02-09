# reorder a array by using
# [1,4,2,5,7] --> [4,2,1,7,5] random order
import random
import math


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reorder(self):
        length = len(self.nums)
        for i in range(length-1, 0, -1):
            index = math.floor(i*random.random())
            temp = self.nums[i]
            self.nums[i] = self.nums[index]
            self.nums[index] = temp

        return self.nums


# test = Solution([1, 5, 6, 7, 8])
# print(test.reorder())


class Solution2(object):    # try to use dictionary to solve this problem, should be more complicated

    def __init__(self, nums):
        self.nums = nums

    def reorder(self):

        my_dir = dict()

        for i in range(len(self.nums)):
            my_dir[random.random()] = self.nums[i]

        key_list = []
        value_list = []

        for key, value in my_dir.items():
            key_list.append(key)

        key_list.sort()

        for key in key_list:
            value_list.append(my_dir[key])

        return value_list


test2 = Solution2([1, 5, 6, 7, 8])
print(test2.reorder())



