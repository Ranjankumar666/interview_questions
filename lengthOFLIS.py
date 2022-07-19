from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    
    def dfs(i, dp):
        if i in dp: 
            return dp[i]
        if i == len(nums)-1:
            return 1
        
        maximum = 0
        
        for k in range(i+1, len(nums)):
            if nums[k] > nums[i]:
                curr = 1 + dfs(k, dp)
                maximum = max(maximum, curr)
                
        
        dp[i] = maximum
        return dp[i]
    
    dp = { len(nums): 1}
    maximum = 0
    for i in range(len(nums)):
        curr = None
        
        if i not in dp:
            curr = dfs(i, dp)
        else:
            curr = dp[i]
        
        maximum = max(curr, maximum)
        
    return maximum


print(lengthOfLIS([10,9,2,5,3,7,101,18]))