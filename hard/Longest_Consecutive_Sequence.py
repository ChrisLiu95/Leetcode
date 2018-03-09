"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""


class Solution(object):
    def longestConsecutive(self, nums):
        mydir = {num: 1 for num in nums}
        res = 0

        for num in nums:
            if not mydir.get(num - 1, 0):
                curr = num
                count = 1
                while mydir.get(curr + 1, 0):
                    count += 1
                    curr += 1
                res = max(count, res)
        return res


test = Solution()
print(test.longestConsecutive([100, 4, 200, 1, 3, 2]))