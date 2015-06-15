class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        row = [1]
        res = []
        if numRows == 1:
            res.append(row)
            return res
        count = 1
        while count < numRows:
            newRow = [1]
            for i in range(1, len(row), 1):
                newRow.append(row[i-1] + row[i])
            newRow.append(1)
            res.append(newRow)
            row = newRow
        return res

s = Solution()
print(s.generate(5))
