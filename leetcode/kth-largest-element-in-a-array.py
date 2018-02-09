# find kth largest element in a array
from heapq import *


class Solution(object):

    def kth_largest_element(self, nums, k):

        nums.sort()
        length = len(nums)
        return nums[length-k]


test = Solution()
print(test.kth_largest_element([1, 2, 3, 4, 5], 2))

'''
heappush(heap,x):x元素插入堆 
heappop(heap):弹出对中最小元素 
heapify(heap):将heap属性强制应用到任意一个列表 
hrapreplace(heap,x):将heap中最小元素弹出，同时x元素入堆 
hlargest(n,iter):返回iter中第n大的元素 
hsmallest(n,iter):返回iter中第n小的元素

use heap to solve the same problem again
'''


class Solution2(object):
    def kth_largest_number(self, nums, k):
        heap = []

        for num in nums:
            heappush(heap, -1*num)

        for _ in range(k):
            re = heappop(heap)

        return -1*re


test2 = Solution2()
print(test2.kth_largest_number([1, 2, 3, 4, 5], 2))
