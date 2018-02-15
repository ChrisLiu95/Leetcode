"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

"""


class Solution(object):
    def wordPattern(self, pattern, str):
        s = str.split()
        return [pattern.find(i) for i in pattern] == [s.index(i) for i in s]


test = Solution()
print(test.wordPattern("abba", "dog cat cat dog"))
