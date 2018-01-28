"""
Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4

There may be more than one sub-arrays with sum as the given sum.
The following solutions print first such sub-array.

"""


class Solution(object):

    def __init__(self, array, given_sum):
        self.array = array
        self.given_sum = given_sum

    def find_sub_array(self):
        current_sum = self.array[0]
        start = 0
        for i in range(1, len(self.array)+1):
            while current_sum > self.given_sum and start < i - 1:
                current_sum = current_sum - self.array[start]
                start += 1
            if current_sum == self.given_sum:
                return [start, i-1]
            current_sum = current_sum + self.array[i]
        print('no sub-array')


test = Solution([1, 4, 5, 3, 10, 5], 10)
print(test.find_sub_array())
