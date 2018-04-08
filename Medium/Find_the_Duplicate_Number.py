"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""

from collections import Counter


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mydir = set()
        # for num in nums:
        #     if num in mydir:
        #         return num
        #     else:
        #         mydir.add(num)
        # return 0

        for num in nums:
            temp = abs(num)
            if nums[temp] < 0:
                return temp
            else:
                nums[temp] *= -1

#         cnt = Counter(nums).most_common()[0][0]
#         return cnt

# left, right = 1, len(nums)-1
# while left < right:
#    mid = (right + left)//2
#    left, right = [left, mid] if sum(i <= mid for i in nums) > mid else [mid+1, right]
# return right

#         s = nums[0]
#         f = nums[nums[0]]
#         while nums[s] != nums[f]:
#             s = nums[s]
#             f = nums[nums[f]]

#         f = 0
#         while nums[f] != nums[s]:
#             f = nums[f]
#             s = nums[s]

#         return nums[f]
