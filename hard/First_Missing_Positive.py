"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.


无序数组的题目如果要O(n)解法往往要用到hash table，但这题要求constant space。所以可以用数组本身作为一个
"hash table"：A[0] = 1, A[1] = 2, .... A[n-1] = n。目标是尽可能将数字i放到数组第i-1个位置。

扫描数组中每个数：
1. 如果A[i]<1或者A[i]>n。说明A[i]一定不是first missing positive。跳过
2. 如果A[i] = i+1，说明A[i]已经在正确的位置，跳过
3. 如果A[i]!=i+1，且0<A[i]<=n，应当将A[i]放到A[A[i]-1]的位置，所以可以交换两数。
这里注意，当A[i] = A[A[i]-1]时会陷入死循环。这种情况下直接跳过。

excited

"""


class Solution(object):
    # (nlgn)
    def firstMissingPositive(self, nums):
        nums.sort()
        res = 1
        for num in nums:
            if num == 1:
                res += 1
        return res

    def firstMissingPositive2(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != i + 1 and 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]  # ！！不能直接交换。必须有temp
            else:
                i += 1
        for j in range(n):
            if nums[j] != j + 1:
                return j + 1
        return n + 1


test = Solution()
print(test.firstMissingPositive2([3, 4, -1, 1]))
