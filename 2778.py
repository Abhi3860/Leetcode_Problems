from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res =0
        n = len(nums)

        for i in range(0,n):
            if n%(i+1) == 0:
                res = res + nums[i]**2
        return res