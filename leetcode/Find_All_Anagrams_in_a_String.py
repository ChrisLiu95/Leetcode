"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will
not be larger than 20,100.

The order of output does not matter.

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

"""
from collections import Counter


class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        a = []
        l = len(p)
        cp = Counter(p)
        cs = Counter(s[:l - 1])

        i = 0
        while i + l <= len(s):
            cs[s[i + l - 1]] += 1
            if cs == cp:
                a.append(i)
            cs[s[i]] -= 1
            if cs[s[i]] == 0:
                del cs[s[i]]
            i += 1
        return a


test = Solution()
print(test.findAnagrams("cbaebabacd", "abc"))
