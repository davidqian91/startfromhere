# class Solution:
#     # @param {string} s
#     # @return {string}
#     def longestPalindrome(self, s):
#         DP = [1 for i in range(len(s))]
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 DP[i] = 2
#             elif i-2 >= 0 and s[i-2] == s[i]:
#                 DP[i] = 3
#             if DP[i-1] != 1:
#                 length = DP[i-1]
#                 if i-length-1 >= 0 and s[i] == s[i-length-1]:
#                     DP[i] = DP[i-1] + 2
#                 else:
#                     l = i - length
#                     r = i
#                     while l < r:
#                         if s[l] != s[r]:
#                             break
#                         l += 1
#                         r -= 1
#                     if l < r:
#                         continue
#                     else:
#                         DP[i] = DP[i-1] +1
#         max = 0
#         pos = -1
#         for i in range(len(s)):
#             if max < DP[i]:
#                 max = DP[i]
#                 pos = i
#         print(DP)
#         print(max, pos)
#         return s[pos-max+1:pos+1]


class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        t = self.prepareString(s)
        p = [0 for i in range(len(t))]
        c = 0; r = 0
        i = 0; j = 0
        for i in range(len(t)):
            j = 2*c - i
            if r > i:
                p[i] = min(r-i, p[j])
            else:
                p[i] = 0
            while i-1-p[i] >= 0 and i+1+p[i] < len(t) and t[i-1-p[i]] == t[i+1+p[i]]:
                p[i] += 1
            if p[i] > r:
                c = i
                r = i+p[i]
        print(t, p)
        m = 0
        index = 0
        for i in range(len(t)):
            if p[i] > m:
                m = p[i]
                index = i
        print(index, m)
        return s[int((index-m)/2):int(index+m+1)/2]

    def prepareString(self, s):
        t = ['#']
        for i in range(len(s)):
            t.append(s[i])
            t.append('#')
        return ''.join(t)

s = Solution()
st = "bananabs"
#######12345654321
print(s.longestPalindrome(st))
