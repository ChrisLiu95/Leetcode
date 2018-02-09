"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

"""


class Solution(object):
    def __init__(self, array):
        self.array = array

    def missing_range(self, lower, upper):
        self.array.insert(0, lower-1)
        self.array.append(upper+1)
        res = []
        i = 0
        while i < len(self.array)-1:
            left, right = self.array[i], self.array[i+1]
            if right-left == 2:
                res.append(str(left+1))
            elif right-left > 2:
                res.append(str(left+1)+"->"+str(right-1))
            i = i+1
        return res


test = Solution([0, 1, 3, 50, 75])
print(test.missing_range(0, 99))

