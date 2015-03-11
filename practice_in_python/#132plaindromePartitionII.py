#132	Palindrome Partitioning II
# use DP
# subproblem: def the minimum cut of A[i..j] is MinCut(i,j)
# MinCut(i,j) = {
#		0  	if A[i..j] is palindrome
#		min{ MinCut(i,k)+ MinCut(k+1,j)+1}	 k =  i...j-1
# }


class Solution:

    #recursive call to find min cut of array s[i...j]
    def minCutRecur(self, s, i, j):
        if self.A[i][j] >= 0:
            return self.A[i][j]
        elif self.isPalindrome(s, i, j):
                return 0
        else:
            self.rcount += 1
            minCount = j
            for k in range(i, j, 1):
                if self.isPalindrome(s, i, k):
                    tmp = 1 + self.minCutRecur(s, k+1, j)
                    if tmp < minCount:
                        minCount = tmp
                else:
                    continue
                self.A[i][j] = minCount
            return minCount

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        self.A = [[-1 for col in range(len(s))] for row in range(len(s))]
        for i in range(len(s)):
            self.A[i][i] = 0
        self.pcount = 0
        self.rcount = 0
        cut = self.minCutRecur(s, 0, len(s)-1)
        print("pcount", self.pcount)
        print("rcount", self.rcount)
        print("minCut", cut)
        return cut

    # find whether a string is palindrome, return boolean
    def isPalindrome(self, s, i, j):
        if self.A[i][j] >= 0:
            return self.A[i][j] == 0
        self.pcount += 1
        #for k in range(i, (i+j+1)/2):
        #    if s[k] != s[i+j-k]:
        #        return False

        self.A[i][j] = 0
        return True


s = Solution()
string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(s.minCut(string))
