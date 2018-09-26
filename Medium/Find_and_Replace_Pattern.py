"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []

        def match(word, pattern):
            if len(word) != len(pattern):
                return False
            dir = {}
            index, Max = 0, len(set(pattern))
            for w, p in zip(word, pattern):
                if w not in dir:
                    dir[w] = p
                    index += 1
                    if index > Max:
                        return False
                else:
                    if dir[w] != p:
                        return False
            return True

        for w in words:
            if match(w, pattern):
                res.append(w)
        return res
