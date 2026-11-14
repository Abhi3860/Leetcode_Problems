import math

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pref_sum = [0] * (n+1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nums[i]

        res = float('inf')
        for i in range(n):
            for j in range(i,n):
                sub_len = j-i+1
                if l<=sub_len<=r:
                    curr_sum = pref_sum[j+1] - pref_sum[i]
                    if curr_sum >0:
                        res = min(res, curr_sum)
        if res == float('inf'):
            return -1
        else: return int(res)