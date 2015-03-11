class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        s = ["" for col in range(10)]
        s[2] = "abc"
        s[3] = "def"
        s[4] = "ghi"
        s[5] = "jkl"
        s[6] = "mno"
        s[7] = "pqrs"
        s[8] = "tuv"
        s[9] = "wxyz"

        stack = []
        result = []
        for i in range(len(digits)):
            d = int(digits[i])
            for j in range(len(s[d])):
                stack.append(s[d][j])
                if i == len(digits)-1:
                    result.append("".join(stack))
                    print(stack)
                    #stack.pop()
                elif j == len(s[d])-1:
                    print(stack)
                    #stack.pop()
        return result

s = Solution()
print(s.letterCombinations("22"))
