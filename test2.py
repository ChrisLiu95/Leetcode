class sellStock(object):
    def stock(self, prices):
        sell1 = 0
        sell2 = 0
        buy1 = -float("inf")
        buy2 = -float("inf")

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2


test = sellStock()
print(test.stock([1, 3, 5, 7]))
