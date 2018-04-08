"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

"""


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # LTE
        res = 0
        for word in words:
            flag = True
            index = 0
            for char in word:
                index = S.find(char, index)
                if index == -1:
                    flag = False
                    break
                index += 1
            if flag:
                res += 1
        return res

