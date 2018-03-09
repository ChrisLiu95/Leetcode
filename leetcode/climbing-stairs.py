# climbing stairs
# it has n stairs to reach the top, each time you can either climb 1 or 2 steps
# find out the numbers of ways to the top


class Solution(object):

    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    # basic Fibonacci Sequence
    def Fibonacci_creator(self, n):
        a, b = 0, 1
        sequence = []
        for i in range(1, n + 1):
            a, b = b, a + b
            sequence.append(a)
        return sequence


r = Solution()
print(r.climbStairs(5))
print(r.Fibonacci_creator(5))
