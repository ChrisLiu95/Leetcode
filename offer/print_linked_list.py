"""
输入一个链表，从尾到头打印链表每个节点的值。
"""


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution(object):
    def printlist(self, head):
        if not head:
            return
        res = []
        while head:
            res.insert(0, head.val)
            head = head.next
        return res
