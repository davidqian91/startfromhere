class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        p = A[0]
        i = 1
        while i < len(A):
            if i >= len(A):
                break
            q = A[i]
            if p == q:
                A.pop(i)
                i -= 1
            elif p < q:
                p = q
            i += 1
        return len(A)

s = Solution()
a = [1, 1, 2]
print(s.removeDuplicates(a))
