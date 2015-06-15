class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.combinationSumRecur(candidates, target)

    def combinationSumRecur(self, candidates, target):
        if not candidates:
            return []
        if candidates[0] > target:
            return []
        res = []
        for i in range(len(candidates)):
            print(res)
            l = []
            if candidates[i] == target:
                l.append(candidates[i])
                if l not in res:
                    res.append(l)
                continue
            elif candidates[i] > target:
                break
            else:
                t = self.combinationSumRecur(candidates[i:], target-candidates[i])
                if not t:
                    continue
                else:
                    for p in t:
                        l = [candidates[i]]
                        l.extend(p)
                        if l not in res:
                            res.append(l)
        return res

s = Solution()
candidates = [1, 1]
print(s.combinationSum(candidates, 1))
