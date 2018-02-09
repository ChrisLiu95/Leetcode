"""
find the number of ways that contiguous numbers sum up to a target number

15: 7,8  4,5,6  1，2，3，4，5 should return 3

假设和为S的连续序列为[a1，a2，……，an]，则可以的到S = a1+a2+…+an，
即S = (a1 + an) * n / 2，这又是等差数列的求和公式，我之前卡在这个公式的原因是没有想到an = a1 + n – 1 这个公式。
由S = (a1 + an) * n / 2和an = a1 + n – 1可以推导出
S = (a1 + a1 + n - 1) * n / 2
===> 2 * a1 + n – 1 = 2 * S / n
===> 2 * a1 = 2S/n – n + 1
===> a1 = (2S/n – n + 1) / 2
因为a1是正整数，而当a1是正整数时，可以得知(2S/n – n + 1) / 2和2S/n也都是正整数。
因为2*a1 > 0，所以2S/n – n + 1 > 0 ===> 2S/n – n >= 0 ===> n * n <= 2S
===> n <= sqrt(2S)，
因为和等于S的连续正数序列至少有两个元素，所以n >= 2。
因此算法的流程就是：依次遍历每一个n(2 <= n <= sqrt(2S))，如果n的值能够满足2S/n和a1 = (2S/n – n + 1) / 2同时为正整数，
则以a1为首元素，长度为n的连续正数序列的和就等于S。
"""
import math


class Solution(object):
    def __init__(self, num):
        self.num = num

    def find_ways(self):
        count = 0
        for n in range(2, int(math.sqrt(2*self.num))+1):
            if (2*self.num) % n == 0:
                if (2*self.num/n-n+1) % 2 == 0:
                    print((2*self.num/n-n+1)/2, n)
                    count = count+1
        return count


test = Solution(15)
print(test.find_ways())
