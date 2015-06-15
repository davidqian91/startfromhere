class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        count = [0 for i in range(128)]
        for i in range(len(s)):
            count[ord(s[i])] += 1
        res = 0
        for i in count:
            if i > 0:
                res += 1
        return res
        
s = Solution()
st = "pwwkew"
print(s.lengthOfLongestSubstring(st))