"""

Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""


class Solution(object):
    def longest(self, str):
        mydic = {}
        for char in str:
            mydic[char] = mydic.get(char, 0) + 1
        res = 0
        for value in mydic.values():
            if value % 2 == 0:
                res += value
            else:
                if value > 1:
                    res += value - 1
        for value in mydic.values():
            if value % 2 == 1:
                return res + 1
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the single letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)


test = Solution()
print(test.longest('ccc'))
