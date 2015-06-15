# class Solution:
#     # @param {string} s
#     # @param {string[]} words
#     # @return {integer[]}
#     def findSubstring(self, s, words):
#         if not s or not words:
#             return []
#         res = []
#         l = len(words[0])
#         step = l*len(words)
#         pos = 0
#         while pos + step <= len(s):
#             if self.findSubstringRecur(s, pos, words, l):
#                 res.append(pos)
#             pos += 1
#         return res

#     def findSubstringRecur(self, s, pos, words, l):
#         p = pos
#         dic = list(words)
#         while p+l <= len(s):
#             t = s[p:p+l]
#             if t in dic:
#                 dic.remove(t)
#                 p = p+l
#                 if not dic:
#                     return True
#             else:
#                 return False
#         if dic:
#             return False
#         else:
#             return True


class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        res = []
        dic = {}
        for d in words:
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1
        l = len(words[0])
        for k in range(l):
            left = k
            count = 0
            newdic = {}
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                #find word
                if tword in dic:
                    if tword in newdic:
                        newdic[tword] += 1
                    else:
                        newdic[tword] = 1
                    count += 1
                    while newdic[tword] > dic[tword]:
                        newdic[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    left = j + l
                    count = 0
                    newdic = {}
        return res
sol = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo","barr","wing","ding","wing"]
# s = "a"
# words = ["a"]
print(sol.findSubstring(s, words))
