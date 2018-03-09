"""
1到n个数组中缺了两个数，如何用O(n)时间，O(1)空间找到这两个数字


Given an array of n unique integers where each element in the array is in range [1, n].
The array has all distinct elements and size of array is (n-2). Hence Two numbers from the
range are missing from this array. Find the two missing numbers.

O(n),O(1)
arrSum => Sum of all elements in the array

sum (Sum of 2 missing numbers) = (Sum of integers from 1 to n) - arrSum
                               = ((n)*(n+1))/2 – arrSum

avg (Average of 2 missing numbers) = sum / 2;
One of the numbers will be less than or equal to avg while the other one will be strictly greater then avg. Two numbers can never be equal since all the given numbers are distinct.
We can find the first missing number as sum of natural numbers from 1 to avg, i.e., avg*(avg+1)/2 minus the sum of array elements smaller than avg
We can find the second missing number as sum of natural numbers from avg+1 to n minus the sum of array elements greater than than avg
Consider an example for better clarification

Input : 1 3 5 6, n = 6
Sum of missing integers = n*(n+1)/2 - (1+3+5+6) = 6.
Average of missing integers = 6/2 = 3.
Sum of array elements less than or equal to average = 1 + 3 = 4
Sum of natural numbers from 1 to avg = avg*(avg + 1)/2
                                     = 3*4/2 = 6
First missing number = 6 - 4 = 2

Sum of natural numbers from avg+1 to n
                                =  n*(n+1)/2 - avg*(avg+1)/2
                                =  6*7/2 - 3*4/2
                                =  15
Sum of array elements greater than average = 5 + 6 = 11
Second missing number = 15 - 11 = 4

"""


class Solution(object):
    # O(n), O(n)
    def missnumber(self, nums):
        temp = [0] * (len(nums) + 2)
        res = []
        for i in range(len(nums)):
            temp[nums[i] - 1] = nums[i]
        for j in range(len(temp)):
            if temp[j] != j + 1:
                res.append(j + 1)
        return res

    # O(n), O(1) 求两个数的avg，两数必然一个比avg小，一个比avg大
    def missnumber1(self, nums):
        length = len(nums) + 2
        total = (1 + length) * length / 2 - sum(nums)
        avg = total // 2
        left = 0
        right = 0
        for i in range(len(nums)):
            if nums[i] <= avg:
                left += nums[i]
            else:
                right += nums[i]
        left = avg * (1 + avg) / 2 - left
        right = (1 + length) * length / 2 - avg * (1 + avg) / 2 - right

        return left, right


test = Solution()
print(test.missnumber1([1, 2, 5, 6]))
