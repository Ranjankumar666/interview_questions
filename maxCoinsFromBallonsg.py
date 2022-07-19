from typing import List


def maxCoins(nums: List[int]) -> int:
    
    def dfs(ballons):
        
        if len(ballons) == 1:
            return  ballons[0]
        
        max_coins = 0
        for i, b in enumerate(ballons):
            curr = dfs(ballons[:i] + ballons[i+1:])
            
            coins = b
            if i - 1 >= 0:
                coins *= ballons[i-1]
            if i + 1 < len(ballons):
                coins *= ballons[i+1]
                
            curr += coins
                
            
            max_coins = max(curr, max_coins)
            
        
        return max_coins
        
    return dfs(nums)
            

print(maxCoins([3,5,8]))    