class Solution:
    # @param {string} s
    # @return {string[]}

    #learn dictionary
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        repeatSet = {}
        resultSet = []
        for i in range(len(s)-9):
            tmpStr = s[i:i+10]
            val = repeatSet.get(tmpStr)
            if val is None:
                repeatSet[tmpStr] = 0
            else:
                if repeatSet[tmpStr] == 0:
                    repeatSet[tmpStr] = 1
                    resultSet.append(tmpStr)
        return resultSet

s = Solution()
testStr = "AAAAAAAAAAA"
print(s.findRepeatedDnaSequences(testStr))
