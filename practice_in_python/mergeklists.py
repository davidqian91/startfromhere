# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return []
        maxint = sys.maxsize
        #build up heap
        heap = MinHeap()
        for i in range(k):
            if not lists[i]:
                heap.insert(ListNode(maxint))
            else:
                heap.insert(lists[i])
        tmp = heap.extractMin()
        head = ListNode(0)
        p = head
        while tmp.val != maxint:
            if not tmp.next:
                heap.insert(ListNode(maxint))
            else:
                heap.insert(tmp.next)
            p.next = tmp
            p = p.next
            tmp = heap.extractMin()
        return head.next


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, node):
        self.heap.append(node)
        self.heapifyup(len(self.heap)-1)
        
    def extractMin(self):
        if not self.heap:
            return None
        p = self.heap.pop()
        if not self.heap:
            return p
        else:
            res = self.heap[0]
            self.heap[0] = p
            self.heapifydown(0)
            return res
    
    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
     
    def heapifyup(self, i):
        while i > 0 and self.heap[i].val < self.heap[int((i-1)/2)].val:
            self.swap(i, int((i-1)/2))
            i = int((i-1)/2)
        
    def heapifydown(self, i):
        while 2 * i + 1 < len(self.heap):
            if 2 * i + 2 == len(self.heap):
                child = 2 * i + 1
            elif self.heap[2 * i + 1].val <= self.heap[2 * i + 2].val:
                child = 2 * i + 1
            else:
                child = 2 * i + 2
            if self.heap[i].val > self.heap[child].val:
                self.swap(i, child)
                i = child
            else:
                break

s = Solution()
a = ListNode(-1)
b = ListNode(2)
l = [b, None, a]
print(s.mergeKLists(l))
