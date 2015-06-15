class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        dic = {}
        m = 0
        n = 0
        for i in range(len(s)):
            if s[i] in dic:
                pos = dic[s[i]]
                if pos >= n:
                    size = i - n
                    m = max(m, size)
                    n = pos+1
            dic[s[i]] = i
        pos = len(s)
        size = pos-n
        m = max(m, size)
        return m

s = Solution()
st = "aa"
print(s.lengthOfLongestSubstring(st))
