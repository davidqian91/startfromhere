class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        res = set()
        uninums = set(nums)
        