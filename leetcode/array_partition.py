"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).


Assume in each pair i, bi >= ai.
Denote Sm = min(a1, b1) + min(a2, b2) + ... + min(an, bn). The biggest Sm is the answer of this problem. Given 1, Sm = a1 + a2 + ... + an.
Denote Sa = a1 + b1 + a2 + b2 + ... + an + bn. Sa is constant for a given input.
Denote di = |ai - bi|. Given 1, di = bi - ai. Denote Sd = d1 + d2 + ... + dn.
So Sa = a1 + a1 + d1 + a2 + a2 + d2 + ... + an + an + dn = 2Sm + Sd => Sm = (Sa - Sd) / 2. To get the max Sm, given Sa is constant, we need to make Sd as small as possible.
So this problem becomes finding pairs in an array that makes sum of di (distance between ai and bi) as small as possible. Apparently, sum of these distances of adjacent elements is the smallest. If that’s not intuitive enough, see attached picture. Case 1 has the smallest Sd.
"""


class Solution(object):
    def maximum_pairs(self, given_array):
        n = len(given_array)
        result = 0
        given_array.sort()
        for i in range(0, n, 2):
            result = result+given_array[i]
        return result


test = Solution()
print(test.maximum_pairs([1, 2, 3, 4, 5, 6]))



