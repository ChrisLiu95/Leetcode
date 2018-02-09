"""
the classic knapsack problem
在01背包问题中，在选择是否要把一个物品加到背包中，必须把该物品加进去的子问题的解与不取该物品的子问题的解进行比较，
这种方式形成的问题导致了许多重叠子问题，使用动态规划来解决。n=5是物品的数量，c=10是书包能承受的重量，w=[2,2,6,5,4]是每个物品的重量，
v=[6,3,5,4,6]是每个物品的价值，先把递归的定义写出来：
            0 ,  i=0 or w=0
c[i,w] =   c[i-1,w]  wi>w
            max((vi+c[i-1,w-wi]),c[i-1,w])  if i>0, wi<w

"""


class solution(object):

    def __init__(self, c, w, v):
        self.c = c
        self.w = w
        self.v = v

    def knapsack(self):
        matrix = [[-1 for _ in range(self.c + 1)] for _ in range(len(self.w) + 1)]
        for j in range(self.c):
            matrix[0][j] = 0
        for i in range(1, len(self.w)+1):
            for j in range(1, self.c + 1):
                matrix[i][j] = matrix[i-1][j]
                if self.w[i - 1] <= j:
                    matrix[i][j] = max(matrix[i][j], matrix[i-1][j-self.w[i-1]]+self.v[i-1])
        return matrix


test = solution(6, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
print(test.knapsack())





