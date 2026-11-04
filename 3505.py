from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)} 
        m = len(vals)

        cnt = [0] * (m + 1)   
        sm = [0] * (m + 1)    

        def update(i: int, dc: int, ds: int) -> None:
            while i <= m:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        def query(i: int):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        LOG = 1
        while (1 << LOG) <= m:
            LOG += 1

        def kth(kk: int) -> int:
            pos = 0
            for p in range(LOG, -1, -1):
                nxt = pos + (1 << p)
                if nxt <= m and cnt[nxt] < kk:
                    pos = nxt
                    kk -= cnt[nxt]
            return pos + 1

        num_windows = n - x + 1
        cost = [0] * num_windows
        total = 0
        med_k = (x + 1) // 2

        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]

            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]

            if i >= x - 1:
                start = i - x + 1
                mi = kth(med_k)
                median = vals[mi - 1]
                c, s = query(mi)
                left = median * c - s
                right = (total - s) - median * (x - c)
                cost[start] = left + right

        INF = float("inf")
        prev = [0] * (n + 1)

        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur

        return prev[n]