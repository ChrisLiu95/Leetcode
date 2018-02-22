"""

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000)
 string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.


find()方法语法：

str.find(str, beg=0, end=len(string))
参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
"""


class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence2(self, s, t):
        start = 0
        for i in range(len(s)):
            start = t.find(s[i], start)
            if start == -1:
                return False
            start += 1
        return True
