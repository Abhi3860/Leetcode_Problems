class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        res = -1
        n = len(nums)
        track = 0
        left = 0 
        right = 0
        win_sum = 0
        t_sum = sum(nums) - x
        if t_sum == 0:
            return len(nums)
        if x==0:
            return 0
        if t_sum < 0:
            return -1
        while right<n:
            win_sum += nums[right]

            while win_sum > t_sum and left <= right:
                win_sum -= nums[left]
                left +=1

            if win_sum == t_sum:
                track = right - left + 1
                res = max(res, track)

            right += 1
            
        if res == -1:
            return -1

        return n - res

