"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity


@cbmbbz In the event that two or more of the lists have the same val, this code will error
out since the queue module will compare the second element in the priority queue which is a
ListNode object (and this is not a comparable type).

To solve for this issue, I have stored (node.val, list_idx, node) to account for this edge case.

!! 加index
"""
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:      # for index, node in enumerate(lists):...
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next
