"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""


class Solution(object):
    # O(n^2)  LTE
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices) - 1, 0, -1):
            for j in range(i):
                res = max(res, prices[i] - prices[j])
        return res

    # O(N) solution
    def maxProfit2(self, prices):
        res, min_price = 0, float('inf')
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            res = max(res, profit)
        return res


test = Solution()
print(test.maxProfit2([7, 1, 5, 3, 6, 4]))
