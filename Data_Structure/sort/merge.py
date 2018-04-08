"""
归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，
每个子序列是有序的。然后再把有序子序列合并为整体有序序列。
首先用Python实现合并两个有序列表的操作。这个非常简单，只要从比较二个列表的第一个数，谁小就先取谁，
取了后就将相应的下标右移一位。然后再进行比较，如果有列表访问结束，那直接将另一个列表的数据依次取出即可。


解决了上面的合并有序列表问题，再来看归并排序，其的基本思路就是将列表分成二组A，B，如果这二组组内的数据都是有序的，
那么就可以很方便的将这二组数据进行排序。如何让这二组组内数据有序了？
可以将A，B组各自再分成二组。依次类推，当分出来的小组只有一个数据时，可以认为这个小组组内已经达到了有序，
然后再合并相邻的二个小组就可以了。这样通过先递归的分解列表，再合并列表就完成了归并排序。

nlog(n)
"""


# coding:utf-8
# 合并有序列表
def mergeList(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


a = [1, 3, 5, 6, 7, 8]
b = [2, 4, 6]
print(mergeList(a, b))


# 拆分列表
def mergeSort(p, first, last):
    new = []
    if first < last:
        mid = (first + last) // 2
        mergeSort(p, first, mid)
        mergeSort(p, mid + 1, last)
        a = p[first:mid + 1]  # 列表的索引性质:列表a中不包含p[mid + 1]元素
        b = p[mid + 1:last + 1]
        new = mergeList(a, b)
        start = first
        for i in new:  # 将合并好的列表复制到p列表相应的位置中
            p[start] = i
            start += 1
    return p


p = [2, 3, 1, 7, 5, 9, 10, 4, 6, 8]
first = 0
last = len(p) - 1
print(mergeSort(p, first, last))
