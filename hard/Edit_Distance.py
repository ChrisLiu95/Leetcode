"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character


classic dp Solution
example
i if j==0
j if i==0
dp("abbc","acc")
= dp("abb","ac")
= 1 + min(("ab","ac"),  # delete b
        ("abb","a") # insert c
        ,("ab", "a") # replace b to c
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = i
        for i in range(n):
            dp[0][i] = i

        for i in range(1, m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j
                if j == 0:
                    dp[i][j] = i
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]
