# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k == 0 or head is None:
            return head
        s = []
        current = head
        s.append(current)
        # use current.next rather than current
        # to fetch the last element in the list
        # rather than a meaningless None
        while(current.next):
            # use to be a mistake:
            # the element added to the stack should be current.next
            s.append(current.next)
            current = current.next
        bottom = current
        newhead = None
        if k % len(s) == 0:
            return head
        for i in range(k % len(s)):
            newhead = s.pop()
        if s:
            bottom.next = head
            tail = s.pop()
            tail.next = None
            return newhead
        else:
            return head
