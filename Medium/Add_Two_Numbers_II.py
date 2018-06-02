"""

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1, x2 = 0, 0
        while l1:
            x1 = x1 * 10 + l1.val
            l1 = l1.next
        while l2:
            x2 = x2 * 10 + l2.val
            l2 = l2.next
        x = x1 + x2

        if x == 0:
            return ListNode(0)

        head = ListNode(0)
        pointer = head
        while x:
            temp, x = x % 10, x // 10
            pointer.next = ListNode(temp)
            pointer = pointer.next
        pointer.next = None
        return self.reverse(head.next)

    def reverse(self, head):
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

test = Solution()
print(test.addTwoNumbers(l1, l2))
