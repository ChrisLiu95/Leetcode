"""
Given a string S and a string T, find the minimum window in S which will contain
 all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique
minimum window in S.

"""

from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        counter = defaultdict(int)
        for char in t:
            counter[char] += 1

        # print(all([True if x <= 0 else False for x in counter.values()]))

        left, right = 0, 0
        minwindow = len(s) + 1
        res = ""

        while right <= len(s):
            # if all character in t are also in s[left:right]
            if all([True if x <= 0 else False for x in counter.values()]):
                if minwindow > right - left:
                    minwindow = right - left
                    # could be better only record the index, could be faster, like res[left, right], where
                    # left and right are indexes
                    res = s[left:right]
                char = s[left]
                if char in counter:
                    counter[char] += 1
                left += 1
            else:
                if right == len(s):
                    break
                char = s[right]
                if char in counter:
                    counter[char] -= 1
                right += 1

        return res


test = Solution()
print(test.minWindow("ADOBECODEBANC", "ABC"))
