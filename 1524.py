class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
     MOD = 10**9 + 7
     odd, even = 0, 1
     parity = 0
     ans = 0
     for x in arr:
         parity ^= x & 1
         if parity:
             ans += even
             odd += 1
         else:
             ans += odd
             even += 1
     return ans % MOD