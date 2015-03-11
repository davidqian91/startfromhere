class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        count = 1
        i = 1
        while True:
            count += 1
            print(A, i)
            if A[i] == A[i-1]:
                while i < len(A)-1 and A[i+1] == A[i]:
                    A.pop(i+1)
            if i >= len(A) - 1:
                break
            i += 1
        return count


class Solution_not_work:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        count = 1
        # for range not work,
        # for range do not dynamically check len(A)
        # once the loop is constructed,
        # len(A) is nevered computed or compared again.
        for i in range(1, len(A), 1):
            count += 1
            if A[i] == A[i-1]:
                while i < len(A)-1 and A[i+1] == A[i]:
                    A.pop(i+1)
                    if i >= len(A) - 1:
                        return count
        return count
