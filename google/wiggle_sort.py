"""

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

"""


class Solution(object):

    @staticmethod
    def wiggle_sort(num):
        num.sort()
        for i in range(1, len(num), 2):
            temp = num[i]
            num[i] = num[i+1]
            num[i+1] = temp
        return num

    def wiggle_sort2(self, num):
        for i in range(len(num)-1):
            if (i % 2 == 0 and num[i] > num[i+1]) or (i % 2 == 1 and num[i] < num[i+1]):
                temp = num[i]
                num[i] = num[i + 1]
                num[i + 1] = temp
        return num


test = Solution()
print(Solution.wiggle_sort([1, 2, 3, 4, 5, 6, 7]))
print(test.wiggle_sort2([1, 5, 9, 6, 4, 8, 10]))

