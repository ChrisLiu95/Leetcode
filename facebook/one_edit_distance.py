"""
Given two strings S and T, determine if they are both one edit distance apart.

one edit distance, there're several cases:
1. modifying
abc --> abe

2. inserting
abc --> abdc

3.
abdc--> abc

4. abc --> abcd

"""


class Solution(object):
    def is_one_distance(self, s, t):
        m, n = len(s), len(t)

        for i in range(min(m, n)):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                elif m > n:
                    return s[i + 1:] == t[i:]
                else:
                    return s[i:] == t[i + 1:]
        return abs(m - n) == 1


test = Solution()
print(test.is_one_distance("adc", "abc"))
