"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3. Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""


class Solution(object):
    def shortest_distance(self, words, word1, word2):
        index1, index2, dis = -1, -1, 1e9
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
                if index2 != -1:
                    dis = min(dis, abs(index1 - index2))
            if word == word2:
                index2 = i
                if index1 != -1:
                    dis = min(dis, abs(index1 - index2))
        return dis


test = Solution()
print(test.shortest_distance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'makes'))
