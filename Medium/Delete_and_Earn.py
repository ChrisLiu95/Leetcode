"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn
by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

"""


class Solution(object):
    def deleteAndEarn(self, nums):

        # dp(i) is the maximum benefit I can obtain using the first i elements in the sorted keys list.
        mydir = {}

        for num in nums:
            mydir[num] = mydir.get(num, 0) + 1

        mykey = list(mydir.keys())
        mykey.sort()
        dp = [0] * (len(mykey) + 1)

        for i in range(len(mykey)):
            dp[i + 1] = max(dp[i],
                            mykey[i] * mydir[mykey[i]] + dp[i if i == 0 or mykey[i] - mykey[i - 1] > 1 else i - 1])

        return dp[-1]
