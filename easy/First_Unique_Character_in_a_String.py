"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""


class Solution(object):
    def firstUniqChar(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(i) for i in letters if s.count(i) == 1]
        print(index)
        return min(index) if len(index) > 0 else -1


test = Solution()
print(test.firstUniqChar("leetcolde"))
