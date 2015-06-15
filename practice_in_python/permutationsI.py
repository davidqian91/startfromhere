class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        res = []
        p = nums
        while p not in res:
            res.append(p)
            p = self.nextPermutation(p)
        return res

    def nextPermutation(self, s):
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        nums = list(s)
        i = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                break
        if i == len(nums)-1:
            swap(nums, i, i-1)
            return nums
        if i == 1 and nums[i-1] >= nums[i]:
            return sorted(nums)
        for j in range(len(nums)-1, i-1, -1):
            if nums[j] > nums[i-1]:
                swap(nums, j, i-1)
                p, q = i, len(nums)-1
                while p < q:
                    swap(nums, p, q)
                    p += 1
                    q -= 1
                return nums

s = Solution()
nums = [0, 1]
print(s.permute(nums))
