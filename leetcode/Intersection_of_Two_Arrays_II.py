"""

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

"""


class Solution(object):
    def intesection(self, nums1, nums2):
        mydir = {}
        res = []
        for i in nums1:
            mydir[i] = mydir.get(i, 0) + 1

        for j in nums2:
            if j in mydir and mydir[j] > 0:
                res.append(j)
                mydir[j] -= 1
        return res


test = Solution()
print(test.intesection([1, 2, 2, 1], [2, 2]))
