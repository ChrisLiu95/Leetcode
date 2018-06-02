"""

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the
average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

"""


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        dp[n][k] stores the maximum sum of average obtained by partitioning the first n numbers in to k groups.
        Within the n numbers, we iteratively exclude the last (n - i) numbers and assume the first i numbers are partitioned in to (k - 1) groups.
        [9,1,2,3,9]
       """
        N = len(A)
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        cur_sum = 0.0
        for i in range(N):
            cur_sum += A[i]
            dp[i + 1][1] = cur_sum / (i + 1)

        for n in range(1, N + 1):
            for k in range(2, K + 1):
                if n < k:
                    continue
                cur_sum = 0.0
                for i in range(n - 1, 0, -1):
                    cur_sum += A[i]
                    dp[n][k] = max(dp[n][k], dp[i][k - 1] + cur_sum / (n - i))

        return dp[N][K]
