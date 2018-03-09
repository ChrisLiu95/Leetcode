"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing
together the nodes of the first two lists.

"""


class Solution(object):

    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 + l2
        elif l1[0] < l2[0]:
            return [l1[0]] + (self.merge(l1[1:], l2))
        else:
            return [l2[0]] + (self.merge(l1, l2[1:]))

    def merge2(self, l1, l2):
        new = []
        while l1 and l2:
            if l1[0] < l2[0]:
                new += [l1[0]]
                l1 = l1[1:]
            else:
                new += [l2[0]]
                l2 = l2[1:]
        if l1:
            return new + l1
        return new + l2

    def merge3(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

# linked list
    # iteratively
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # recursively
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


test = Solution()
print(test.merge([1, 3, 5], [2, 4, 6]))
print(test.merge2([1, 3, 4], [2, 9]))
