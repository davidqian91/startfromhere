#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
        parent = None
        current = head
        while current:
            child = current
            #find the last child of the same values list
            while child.next and child.next.val == current.val:
                child = child.next

            if child != current:
                #dulicate values:
                if current.val == head.val:
                    head = child.next
                    current = head
                else:
                    current = child.next
                    parent.next = child.next
            else:
                parent = current
                current = current.next

        return head


s = Solution()
a = ListNode(1)
b = ListNode(1)
a.next = b
s.deleteDuplicates(a)
