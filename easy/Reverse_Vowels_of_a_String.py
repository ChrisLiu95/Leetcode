"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".



"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # LTE
        # vowels: a,e,i,o,u
        #         set = ["a","e","i","o","u","A","E","I","O","U"]
        #         seen = []

        #         for index,char in enumerate(s):
        #             if char in set:
        #                 seen.append(char)

        #         seen = seen[::-1]
        #         j = 0
        #         ss=""

        #         for i in range(len(s)):
        #             if s[i] in set:
        #                 ss+=seen[j]
        #                 j+=1
        #             else:
        #                 ss+=s[i]
        #         return ss

        # two pointer method O(n)

        left = 0
        right = len(s) - 1
        s = list(s)
        vowels = "AEIOUaeiou"

        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)
