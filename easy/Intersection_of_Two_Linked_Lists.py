"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        def listlength(head):
            length = 1
            while head:
                head = head.next
                length += 1
            return length

        len1 = listlength(headA)
        len2 = listlength(headB)

        if len1 > len2:
            while len1 != len2:
                headA = headA.next
                len1 -= 1
        else:
            while len1 != len2:
                headB = headB.next
                len2 -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA
