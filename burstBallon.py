from functools import lru_cache
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums[]
        N= len(nums)
        table = [ [0 for j in range(N) ] for i in range(N)]
        
        for i in range(N):
            temp = nums[i]
            if i - 1>= 0:
                temp *= nums[i-1]
            if i + 1 < N:
                temp *= nums[i+1]

            table[i][i] = temp
            
        
        for i in range(N):
            for j in range(N):
                if i == j: continue

                maxVal =0 
                for k in range(i, j+1):
                    cost = 0
                    if i <= k-1:
                        cost += table[i][k-1] 
                    if  k+1 <= j:
                        cost += table[k+1][j]

                    curr =  nums[k]

                    if i - 1 >= 0:
                        curr *= nums[i-1]

                    if j + 1 < N:
                        curr *= nums[j+1]

                    curr += cost
                    maxVal = max(maxVal, curr)

                table[i][j]= maxVal
                        
                    

        print(table)
        return table[0][N-1]


print(Solution().maxCoins([3, 1, 5, 8]))