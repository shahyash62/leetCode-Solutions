# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listNode = head
        pointers = []
        x=0
        while(listNode != None):
            x += 1
            listNode = listNode.next
        if(x == n):
            head = head.next
            return head
        y = 0
        now = 0
        nex = 0
        listNode = head
        while(y < x):
            if (y == ((x-n)-1)):
                now = listNode
            if (y == (x-n)):
                nex = listNode.next
            listNode = listNode.next
            y += 1
        now.next = nex
        return head
