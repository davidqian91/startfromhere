# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        count = 1
        p = head
        p1 = None
        while p is not None and count < m:
            count += 1
            p1 = p
            p = p.next
        if p is None:
            return None
        st = []
        while p is not None and count <= n:
            st.append(p)
            count += 1
            p = p.next
        p2 = p
        if p1 is None and st:
            head = st.pop()
            p = head
        else:
            p = p1
        while st:
            t = st.pop()
            p.next = t
            p = t
        p.next = p2
        return head

s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print(s.reverseBetween(a, 2, 3))
