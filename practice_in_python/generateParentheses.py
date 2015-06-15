class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n < 1:
            return []
        if n == 1:
            return ["()"]
        DP = [set() for i in range(n+1)]
        DP[1].add("()")
        for i in range(2, n+1, 1):
            for j in DP[i-1]:
                DP[i].add("("+j+")")
            for j in range(1, i):
                for p in DP[j]:
                    for q in DP[i-j]:
                        DP[i].add(p + q)
        return DP[n]

s = Solution()
print(len(s.generateParenthesis(5)))
