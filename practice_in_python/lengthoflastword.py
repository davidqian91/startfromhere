class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        b, lastIndex = False, len(s)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if b:
                    return lastIndex - i
            else:
                if not b:
                    b, lastIndex = True, i
        if b:
            return lastIndex
        else:
            return 0
