"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
For example, given array S = [-1, 0, 1, 2, -1, -4], A solution set is:
[ [-1, 0, 1],
[-1, -1, 2]]
"""


class Solution(object):
    def __init__(self, given_array):
        self.given_array = given_array

    def sum(self):
        length = len(self.given_array)
        new_array = sorted(self.given_array)
        result_set = []
        final = []
        if length < 3:
            return False
        for i in range(length-2):
            if new_array[i] > 0:
                break
            j = i + 1
            k = length-1
            while j < k:
                result = new_array[i]+new_array[j]+new_array[k]
                if result == 0:
                    result_set.append([new_array[i], new_array[j], new_array[k]])
                    k = k - 1
                    j = j + 1
                elif result > 0:
                    k = k - 1
                else:
                    j = j + 1

        for items in result_set:
            if items in final:
                pass
            else:
                final.append(items)
        return final


test = Solution([-1, 0, 1, 2, -1, -4])
print(test.sum())


