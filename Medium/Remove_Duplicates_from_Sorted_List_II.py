"""

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only
distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        temp = dummy
        repeat = False

        while head and head.next:
            if head.val != head.next.val:
                if not repeat:
                    temp.next = head
                    temp = temp.next
                repeat = False
            else:
                repeat = True
            head = head.next
        temp.next = None if repeat else head
        return dummy.next
