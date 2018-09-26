"""
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        list = []

        while head:
            list.append(head.val)
            head = head.next

        newlist = [list.pop()]

        while list:
            temp = list.pop()
            if temp <= newlist[0]:
                newlist = [temp] + newlist
                continue
            elif temp >= newlist[-1]:
                newlist = newlist + [temp]
                continue
            for i in range(len(newlist) - 1):
                if newlist[i] <= temp <= newlist[i + 1]:
                    newlist = newlist[:i + 1] + [temp] + newlist[i + 1:]
                    break

        newlist = newlist[::-1]
        res = dummy = ListNode(0)
        while newlist:
            temp = newlist.pop()
            dummy.next = ListNode(temp)
            dummy = dummy.next

        return res.next
