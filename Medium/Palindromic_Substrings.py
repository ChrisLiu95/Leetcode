"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even
they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        res = 0

        for i in range(length):
            res += (self.check(i, i, s) + self.check(i, i + 1, s))
        return res

    def check(self, x, y, s):
        count = 0
        while x >= 0 and y < len(s):
            if s[x] != s[y]:
                return count
            else:
                count += 1
            x -= 1
            y += 1
        return count
