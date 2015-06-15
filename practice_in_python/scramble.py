class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    # T(n) = T(n-1)T(1) + T(n-2)T(2)
    # def isScramble(self, s1, s2):
    #     print(s1, s2)
    #     n = len(s1)
    #     m = len(s2)
    #     if n != m:
    #         return False
    #     if n <= 1:
    #         return s1 == s2
    #     r = int(n/2)
    #     return (self.isScramble(s1[:r], s2[:r]) and self.isScramble(s1[r:], s2[r:])) or (self.isScramble(s1[:n-r], s2[:n-r]) and self.isScramble(s1[n-r:], s2[n-r:])) or (self.isScramble(s1[:r], s2[n-r:]) and self.isScramble(s1[r:], s2[:n-r])) or (self.isScramble(s1[:n-r], s2[r:]) and self.isScramble(s1[n-r:], s2[:r]))

    def isScramble(self, s1, s2):
        n = len(s1)
        if s1 == s2:
            return True
        count = [0 for i in range(26)]
        for i in range(n):
            count[ord(s1[i])-ord('a')] += 1
            count[ord(s2[i])-ord('a')] -= 1
        for i in count:
        	if i != 0:
        		return False
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True
        return False

s = Solution()
s1 = "abcdefghijklmn"
s2 = "efghijklmncadb"
print(s.isScramble(s1, s2))
