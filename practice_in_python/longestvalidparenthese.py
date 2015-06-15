# class Solution:
#     # @param s, a string
#     # @return an integer
#     def longestValidParentheses(self, s):
#         length = len(s)
#         if length < 2:
#             return 0
#         M = [[False for col in range(length)] for row in range(length)]
#         for i in range(length-1):
#             if s[i] == '(' and s[i+1] == ')':
#                 M[i][i+1] = True
#         for l in range(3, length-1, 2):
#             for i in range(length - l):
#                 if s[i] == ')' or s[i+l] == '(':
#                     continue
#                 for k in range(1, l, 2):
#                     if M[i][i+k] and M[i+k+1][i+l]:
#                         M[i][i+l] = True
#                         break
#                 if not M[i][i+l]:
#                     M[i][i+l] = M[i+1][i+l-1]
#         for l in range(length-1, 0, -1):
#             for i in range(length - l):
#                 if M[i][i+l]:
#                     return l+1
#         return 0


# class Solution:
#     # @param s, a string
#     # @return an integer
#     def longestValidParentheses(self, s):
#         max = 0
#         cur = 0
#         st = 0
#         for v in s:
#             if v == '(':
#                 st += 1
#             else:
#                 if st == 0:
#                     if max < cur:
#                         max = cur
#                     cur = 0
#                     st = 0
#                     continue
#                 else:
#                     st -= 1
#                     cur += 2
#         return max


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if len(s) <= 1:
            return 0
        stack = 0
        max_ = [0]*len(s)
        maxlen = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack += 1
            if c == ')':
                if stack > 0:
                    stack -= 1
                    max_[i] = max_[i-1] + 2
                    if i - max_[i] >= 0:
                        max_[i] += max_[i - max_[i]]
            maxlen = max(max_[i], maxlen)
        print(max_)
        return maxlen

s = Solution()
l = "()(()"
# l = "()())()(())))(()))))()())(()))()()()))()()()))))(((()))()))()()))))(()))((()))())))(()()((()())))()))(()()()()(((((()))))))))(((())))((()()))())(())))((()))))))()())()()))())()))((((()()()(()()"
print(s.longestValidParentheses(l))
