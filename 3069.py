from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        x = int(len(nums))
        k,j=1,1
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2,x):
            if arr1[j-1]>arr2[k-1]:
                arr1.append(nums[i])
                j=j+1
            else:
                arr2.append(nums[i])
                k=k+1
        result = arr1 + arr2
        return result
        

        