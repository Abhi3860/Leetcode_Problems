from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        res = -1
        n = len(nums)
        freq = Counter(nums)
        if k == n:
            for i in nums:
                if i> res:
                    res = i
            return res

        if k == 1:
            large = [num for num, count in freq.items() if count == 1]
            return max(large, default=-1)

        if k>1 & k<n:
            start_count = freq[nums[0]]
            end_count = freq[nums[n-1]]
            if start_count == 1 and end_count ==1:
                return max(nums[0], nums[n-1])
            elif start_count ==1 and end_count >1:
                return nums[0]
            elif start_count >1 and end_count==1:
                return nums[n-1]
            else:
                return -1
