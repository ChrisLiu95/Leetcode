"""
在刘慈欣科幻小说《三体》中提到水滴飞行器攻击对四维空间无效。假设人类捕获了一台水滴飞行器，
水滴飞行器在人类手中只能在某个位置进行“一次”同时朝四个直线方向对敌方舰队攻击，攻击后该位置的四个方向的敌方战舰都能被摧毁（
含水滴飞行器所在位置的敌方战舰）；但如果碰到四维空间后，该方向后续攻击则无效；另外，如果水滴飞行器所在位置为四维空间时，
攻击同样无效。若某星球的舰队整齐部署在四维空间周围，人类需要利用仅有的一次机会对该舰队发动攻击。为了简化问题，
使用矩阵描述该星球的舰队部署情况：其中”1“表示战舰，”0“表示四维空间。水滴飞行器直线攻击方式为正上、正下、正左和正右。
请用最快的速度计算出水滴飞行器要移动到矩阵中的什么位置（可有多个）才能摧毁最多的战舰。

11111
01010
10111
00011

"""


class Solution(object):
    def findPosition(self, m, n, matrix):
        matrixright = [[0] * n for _ in range(m)]
        matrixleft = [[0] * n for _ in range(m)]
        matrixup = [[0] * n for _ in range(m)]
        matrixdown = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrixright[i][j] = 0
                else:
                    while matrix[i][j + 1] == 1 and j + 1 < n:
                        matrixright[i][j] += 1
                        j += 1

        for i in range(m):
            for j in range(n - 1, -1, 0):
                if matrix[i][j] == 0:
                    matrixleft[i][j] = 0
                else:
                    while matrix[i][j - 1] == 1 and j - 1 > 0:
                        matrixleft[i][j] += 1
                        j -= 1

        for i in range(n):
            for j in range(m):
                if matrix[j][i] == 0:
                    matrixdown[j][i] = 0
                else:
                    while matrix[j + 1][i] == 1 and j + 1 < m:
                        matrixdown[j][i] += 1
                        j += 1

        for i in range(n):
            for j in range(m - 1, -1, 0):
                if matrix[i][j] == 0:
                    matrixup[i][j] = 0
                else:
                    while matrix[i][j - 1] == 1 and j - 1 > 0:
                        matrixup[i][j] += 1
                        j -= 1

        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    temp = matrixup[i][j] + matrixleft[i][j] + matrixright[i][j] + matrixdown[i][j]
                    if temp > res:
                        res.pop()
                        res.append([i, j])
        return res
