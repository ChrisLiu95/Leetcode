"""
Given a string S and a character C, return an array of integers representing the shortest distance
from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

"""


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexlist = [index for index, char in enumerate(S) if char == C]

        res = []

        for index, char in enumerate(S):
            mindis = min([abs(index - i) for i in indexlist])
            res.append(mindis)

        return res
