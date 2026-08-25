from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
       nset = set(nums)

       j=1

       while j*k in nset:
           j=j+1
       return j*k 
    
z = [8,2,3,4,6]
sol = Solution()
a = sol.missingMultiple(z,2)
print(a)