import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))          # min-heap of free server ids (already sorted = valid heap)
        busy = []                      # min-heap of (end_time, server_id)
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            # Release servers that have finished by the time this request arrives
            while busy and busy[0][0] <= start:
                _, sid = heapq.heappop(busy)
                # Re-insert with offset so ordering starts from i % k
                heapq.heappush(free, i + ((sid - i) % k))

            if not free:
                continue               # all servers busy, drop the request

            # Pop the free server that is first at or after i % k (circularly)
            slot = heapq.heappop(free)
            sid = slot % k
            count[sid] += 1
            heapq.heappush(busy, (start + dur, sid))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]