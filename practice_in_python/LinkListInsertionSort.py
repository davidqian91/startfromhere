class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head:
            return None
        p = head
        q = p.next
        while q:
            if q.val >= p.val:
                p = p.next
                q = q.next
                continue
            if head.val > q.val:
                p.next = q.next
                q.next = head
                head = q
                q = p.next
                continue
            t = head
            while t != p:
                if t.next.val > q.val:
                    break
                t = t.next
            if t == p:
                p = p.next
                q = q.next
            else:
                p.next = q.next
                q.next = t.next
                t.next = q
                q = p.next
        return head
    
# class Solution:
#     # @param {ListNode} head
#     # @return {ListNode}
#     def insertionSortList(self, head):
#         if not head:
#             return None
#         st = [head]
#         q = head.next
#         while q:
#             p = st[len(st)-1]
#             if p.val <= q.val:
#                 p = p.next
#                 q = q.next
#                 continue
#             t = p
#             while st and t.val > q.val:
#                 t = st.pop()
#             if st:
#                 p.next = q.next
#                 q.next = t.next
#                 t.next = q
#                 q = p.next
#                 while t != q:
#                     st.append(t)
#                     t = t.next
#             else:
#                 p.next = q.next
#                 q.next = head
#                 head = q
#                 q = p.next
#                 t = head
#                 while t != q:
#                     st.append(t)
#                     t = t.next

    def init(self, l):
        if not l:
            return None
        head = ListNode(l[0])
        p = head
        for v in l[1:]:
            q = ListNode(v)
            p.next = q
            p = q
        return head

s = Solution()
head = s.init([1, 1])
s.insertionSortList(head)
