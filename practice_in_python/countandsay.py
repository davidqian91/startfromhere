class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        s = "1"
        for i in range(1, n):
            s = self.calcnext(s)
        return ''.join(s)

    def calcnext(self, s):
        p = 0
        res = []
        while p < len(s):
            l = 1
            while p + l < len(s) and s[p] == s[p+l]:
                l += 1
            res.append(l)
            res.append(s[p])
            p += l
        ans = ""
        for i in res:
            ans += str(i)
        return ans

s = Solution()
print(s.countAndSay(10))
