class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        self.DP = [[0 for i in range(len(p)+1)] for j in range(len(s)+1)]
        return self.isMatchRecur(s+'#', 0, p+'#', 0)

    def isMatchRecur(self, s, i, p, j):
        print(s[i:], p[j:])
        if i == len(s) and j == len(p):
            return True
        if i >= len(s) or j >= len(p):
            return False
        if self.DP[i][j] != 0:
            return self.DP[i][j] > 0
        c = p[j]
        if len(p) > j+1 and p[j+1] == '*':
            if c == '.' or c == s[i]:
                b = self.isMatchRecur(s, i, p, j+2) or self.isMatchRecur(s, i+1, p, j+2) or self.isMatchRecur(s, i+1, p, j)
                if b:
                    self.DP[i][j] = 1
                else:
                    self.DP[i][j] = -1
                return b
            else:
                b = self.isMatchRecur(s, i, p, j+2)
                if b:
                    self.DP[i][j] = 1
                else:
                    self.DP[i][j] = -1
                return b
        else:
            if c == '.' or c == s[i]:
                b = self.isMatchRecur(s, i+1, p, j+1)
                if b:
                    self.DP[i][j] = 1
                else:
                    self.DP[i][j] = -1
                return b
            else:
                self.DP[i][j] = -1
                return False

s = Solution()
print(s.isMatch("a", "ab*"))
