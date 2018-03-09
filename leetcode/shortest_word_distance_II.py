"""

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words
and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words
word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""
import collections


class Solution(object):
    def __init__(self, words):
        self.words = words
        self.dic = collections.defaultdict(list)
        for i, word in enumerate(self.words):
            self.dic[word].append(i)

    def shortest(self, word1, word2):
        index1 = self.dic[word1]
        index2 = self.dic[word2]
        i, j, dist = 0, 0, float("inf")
        while i < len(index1) and j < len(index2):
            dist = min(dist, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1

        return dist


test = Solution(["practice", "makes", "perfect", "coding", "makes"])
print(test.shortest("coding", "practice"))
print(test.shortest("coding", "makes"))
