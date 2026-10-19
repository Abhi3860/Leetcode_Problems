class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        for c,i in enumerate(nums):
            if i == target:
                res.append(c)
        return res
        