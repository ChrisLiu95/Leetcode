"""

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""

import collections


class Solution(object):
    def isAnagram(self, s, t):
        counts = collections.Counter(s)
        countt = collections.Counter(t)

        return countt == counts


test = Solution()
print(test.isAnagram("anagram", "nagaram"))