"""

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

We can use the standard two-pointer approach that starts at the left and right
of the string and move inwards. Whenever there is a mismatch, we can either exclude
 the character at the left or the right pointer. We then take the two remaining substrings
  and compare against its reversed and see if either one is a palindrome.
"""


class Solution(object):
    # slow, can not deal with very long input str
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            temp = s[:i] + s[i + 1:]
            if temp == temp[::-1]:
                return True
        return False

    def validPalindrome2(self, s):
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True


test = Solution()
print(test.validPalindrome("abad"))
