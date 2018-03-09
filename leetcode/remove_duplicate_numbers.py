"""
Given a sorted array, remove the duplicates in place such that each element appear only once and
 return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
"""


# use filter function


class Solution(object):
    def __init__(self, array):
        self.array = array

    def remove_duplicate(self):
        my_dir = []
        count = 0
        for i in range(len(self.array)):
            if self.array[i] in my_dir:
                count += 1
                self.array[i] = 0
            else:
                my_dir.append(self.array[i])
        while 0 in self.array:
            self.array.remove(0)

        return self.array, len(self.array) - count


test = Solution([1, 3, 3, 4, 4, 5])
print(test.remove_duplicate())


def solution2(nums):
    i = 1
    for j in range(len(nums)):
        if nums[i - 1] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return len(nums[:i])


def solution3(nums):
    s, total = 1, len(nums)
    while s < total:
        if nums[s] == nums[s - 1]:
            nums.pop(s)
            total -= 1
        else:
            s += 1
    return len(nums)
