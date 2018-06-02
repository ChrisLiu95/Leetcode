"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

"""

from collections import Counter


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # set method, LTE, too slow
        if len(s) <= 10:
            return []

        res = set()
        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if s.find(temp, i + 1) != -1:
                res.add(temp)

        return list(res)

        # using collection Counter

    def findRepeatedDnaSequences2(self, s):
        if len(s) > 10:
            mydir = Counter([s[i:i + 10] for i in range(len(s) - 9)])
            return [key for key in mydir.keys() if mydir[key] > 1]
        else:
            return []

    # set method  fast
    def findRepeatedDnaSequences3(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        ret = set()
        seq_map = set()
        for i in range(n-9):
            seq = s[i:i+10]
            if seq in seq_map:
                ret.add(seq)
            else:
                seq_map.add(seq)
        return list(ret)