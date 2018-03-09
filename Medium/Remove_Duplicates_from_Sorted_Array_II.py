"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.


"""


class Solution(object):
    # slow
    def removeDuplicates(self, nums):
        l, r = 2, len(nums)

        while l < r:
            if nums[l] == nums[l - 1] and nums[l] == nums[l - 2]:
                nums.pop(l)
                r -= 1
            else:
                l += 1
        return nums

    def removeDuplicates2(self, nums):
        if len(nums) <= 2:
            return len(nums)
        prev = 1

        for i in range(2, len(nums)):
            if nums[i] == nums[prev] and nums[i] == nums[prev - 1]:
                continue
            else:
                prev += 1
                nums[prev] = nums[i]
        return prev + 1


test = Solution()
print(test.removeDuplicates2([1, 1, 1, 2, 2, 3]))
