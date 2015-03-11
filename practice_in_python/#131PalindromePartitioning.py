
##Given a string s, partition s such that every
#substring of the partition is a palindrome.
#Return all possible palindrome partitioning of s.
#
# solution: first find all the possbile palindrome strings,
# P[j][i] = True if string s[j..i] is palindrome
# P[j][i] = P[j+1][i-1] enables us to benefit from the previous calculation
# then calculate all the possbile partitions
# A[i] contains the indices of the last palindrome string in
# all the possible partition
# As an example, if A[2] = [0,2], then the possible partitions are
# s[0..2] is palindrome, and s[2] is palindrome
# Since A[i] also give us the last indices of possbile partitions,
# We can find a valid partition by recusively check A[i]
# Note that the structure from top A[n] to A[0] is similar to a tree,
# To output all the palindrome strings, use a stack to store the trace of the
# path in the tree, which is the indices of the partition.
# 

class Solution:
    def partition(self, s):
        P = [[False for row in range(len(s))] for col in range(len(s))]
        A = [[] for row in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if i == j:
                    P[j][i] = True
                elif s[i] != s[j]:
                    P[j][i] = False
                elif i == j + 1:
                    P[j][i] = True
                else:
                    P[j][i] = P[j+1][i-1]
                if P[j][i]:
                    A[i].append(j)
        self.stack = []
        self.solution = []
        self.recurPrint(s, A, len(s)-1)
        return self.solution

    def recurPrint(self, s, A, n):
        if n == -1:
            tstr = []
            tmp = None
            for idx in self.stack[::-1]:
                if tmp is not None:
                    tstr.append(s[tmp:idx])
                tmp = idx
            tstr.append(s[tmp:len(s)])
            self.solution.append(tstr)
            return
        for i in A[n]:
            self.stack.append(i)
            self.recurPrint(s, A, i-1)
            self.stack.pop()

sol = Solution()
print(sol.partition("aabb"))
