"""
A string S of lowercase letters is given. We want to partition this string into as many parts as
possible so that each letter appears in at most one part, and return a list of integers representing
the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

Time complexity: O(n)
space complexity: O(n)

"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []

        last_index = {}

        for i in range(len(S) - 1, -1, -1):
            if S[i] not in last_index:
                last_index[S[i]] = i

        res = []
        i = 0

        while i < len(S):
            span = 1
            j = last_index[S[i]]
            while i != j:
                i += 1
                span += 1
                j = max(j, last_index[S[i]])
            i += 1
            res.append(span)

        return res
