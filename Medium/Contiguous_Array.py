"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

解析：
To find the maximum length, we need a dict to store the value of count (as the key) and its
associated index (as the value). We only need to save a count value and its index at the first time,
when the same count values appear again, we use the new index subtracting the old index to calculate
the length of a subarray. A variable max_length is used to to keep track of the current maximum length.

count = 0
遇到0减一，遇到1加1， 用一个字典记录，键为count值， value为index， count相同则说明index之间的1，0个数一样多
"""


class Solution(object):
    def findMaxLength(self, nums):
        if not nums:
            return 0

        mydir = {0: 0}
        res = 0
        count = 0

        # >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        # >>>list(enumerate(seasons))
        # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
        # >>>list(enumerate(seasons, start=1))       # 小标从 1 开始
        # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            if num == 1:
                count += 1
            if count in mydir:
                res = max(res, index - mydir[count])
            else:
                mydir[count] = index

        return res
