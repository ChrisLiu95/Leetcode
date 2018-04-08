"""
Counting sort (sometimes referred to as ultra sort or math sort[1]) is a sorting algorithm which
(like bucket sort) takes advantage of knowing the range of the numbers in the array to be sorted (array A).
It uses this range to create an array C of this length. Each index i in array C is then used to count how many
 elements in A have the value i; then counts stored in C can then be used to put the elements in A into their
  right position in the resulting sorted array.

适用于小范围排序， O（n）, 但需要开辟额外空间， 不适于大规模排序
适用于知道数组范围（已知最大值，最小值）
"""


# nums = [3,1,2,4,6,5,5]
class Solution(object):
    def counting_sort(self, nums, max, min):
        temp = [0] * (max - min + 1)

        for num in nums:
            temp[num - min] += 1
        print(temp)
        res = []
        for index, val in enumerate(temp):
            res += [index + min] * val
        return res


test = Solution()
print(test.counting_sort([3, 1, 1, 2, 4, 6, 6, 5, 5], 6, 1))
