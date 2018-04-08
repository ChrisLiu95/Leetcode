"""
Write a function to find the longest common prefix string amongst an array of strings.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        res = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[:-1]
        return res
