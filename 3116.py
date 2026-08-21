import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % f == 0 for f in filtered_coins):
                filtered_coins.append(c)
        coins = filtered_coins
        
        n = len(coins)
        high_bound = k * coins[0]
        
        add_lcms = []
        sub_lcms = []
        
        def generate_subsets(idx: int, current_lcm: int, size: int):
            if size > 0:
                if size % 2 == 1:
                    add_lcms.append(current_lcm)
                else:
                    sub_lcms.append(current_lcm)
            
            for i in range(idx, n):
                next_lcm = math.lcm(current_lcm, coins[i])
                

                if next_lcm <= high_bound:
                    generate_subsets(i + 1, next_lcm, size + 1)
        
        generate_subsets(0, 1, 0)
        
        def count_valid(x: int) -> int:
            res = 0
            for l in add_lcms:
                res += x // l
            for l in sub_lcms:
                res -= x // l
            return res

        low = 1
        high = high_bound
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if count_valid(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans