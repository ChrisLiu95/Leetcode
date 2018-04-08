"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False

"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True

        if "A" <= word[0] <= "Z":
            if "A" <= word[1] <= "Z":
                for i in range(2, len(word)):
                    if not "A" <= word[i] <= "Z":
                        return False
                return True
            else:
                for i in range(2, len(word)):
                    if "A" <= word[i] <= "Z":
                        return False
                return True
        else:
            for i in range(1, len(word)):
                if "A" <= word[i] <= "Z":
                    return False
            return True
