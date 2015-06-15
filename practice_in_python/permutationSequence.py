class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        fac = [1]
        for i in range(1, n, 1):
            fac.append(fac[i-1] * i)
        nums = list(range(1, n+1))
        res = ""
        for l in range(n-1, -1, -1):
            j = int((k-1)/fac[l])
            k = k-fac[l]*j
            res += str(nums.pop(j))
        return res

s = Solution()
print(s.getPermutation(2, 2))
