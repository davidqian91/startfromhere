class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        length = len(s)
        if length < 2:
            return 0
        M = [[False for col in range(length)] for row in range(length)]
        for i in range(length-1):
            M[i][i+1] = s[i] != s[i+1]
        for l in range(3, length-1, 2):
            for i in range(length - l):
                if s[i] == ')' or s[i+l] == '(':
                    continue
                for k in range(1, l, 2):
                    if M[i][i+k] and M[i+k+1][i+l]:
                        M[i][i+l] = True
                        break
                if not M[i][i+l]:
                    M[i][i+l] = M[i+1][i+l-1]
        for l in range(length-1, 0, -1):
            for i in range(length - l):
                if M[i][i+l]:
                    return l+1
        return 0

 ##DP , TLE
s = Solution()
print(s.longestValidParentheses(")()(((())))))"))
