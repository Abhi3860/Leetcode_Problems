class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = -1
        inst = 0
        for i in range(0,n):
            start = max(nums[0:i+1])
            end = min(nums[i:n])
            inst = start - end
            if inst<=k:
                res = i
                break

        return res
