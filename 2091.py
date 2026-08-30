from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = 0
        max_idx = 0

        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        min_del = min(min_idx + 1, n - min_idx)
        max_del = min(max_idx + 1, n - max_idx)

        return min(min_del + max_del,
                   max(min_idx, max_idx) + 1,
                   n - min(min_idx, max_idx))
