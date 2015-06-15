class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        count = 1
        p = head
        while p is not None and count < m:
            count += 1
            p = p.next
        if p is None:
            return None
        p1 = p
        st = []
        while p is not None and count < n:
            st.append(p)
            count += 1
            p = p.next
        if p is None:
            return None
        p2 = p.next
        p = p1
        while st:
            t = st.pop()
            p.next = t
            p = t
        p.next = p2
        return head
