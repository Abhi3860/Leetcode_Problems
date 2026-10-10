class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        low, high = 0, max(diff)

        while low < high:
            mid = (low + high) // 2
            needed = sum(max(0, d - mid) for d in diff)

            if needed <= k:
                high = mid
            else:
                low = mid + 1

        cap = low

        for i in range(len(diff)):
            if diff[i] > cap:
                k -= diff[i] - cap
                diff[i] = cap

        for i in range(len(diff)):
            if k == 0:
                break
            if diff[i] == cap:
                diff[i] -= 1
                k -= 1

        return sum(d * d for d in diff)