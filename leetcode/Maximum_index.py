"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

Example :

A : [3 5 4 2]

Output : 2
for the pair (3, 4)

"""


class Solution(object):
    def __init__(self, given_array):
        self.given_array = given_array

    def maxIndexDiff(self):
        n = len(self.given_array)
        maxDiff = -1
        for i in range(0, n):
            j = n - 1
            while j > i:
                if self.given_array[j] > self.given_array[i] and maxDiff < (j - i):
                    maxDiff = j - i
                j -= 1

        return maxDiff


test = Solution([9, 2, 3, 4, 5, 6, 7, 8, 18, 0])
print(test.maxIndexDiff())

