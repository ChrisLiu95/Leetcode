"""
先从待排序的数组中找出一个数作为基准数（取第一个数即可），然后将原来的数组划分成两部分：
小于基准数的左子数组和大于等于基准数的右子数组。然后对这两个子数组再递归重复上述过程，直到两个子数组的所有数都分别有序。最后返回“左子数组” + “基准数” + “右子数组”，即是最终排序好的数组。

O(nlogn)

"""


# 实现快排
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    # 递归调用
    return quicksort(less) + [base] + quicksort(greater)


def main():
    nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(quicksort(nums))


main()
