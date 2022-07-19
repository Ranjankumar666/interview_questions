def maxSumIS(nums, n):
		# code here
        def dfs(i, dp ={}):
            if i in dp: return dp[i]
            
            maximum = 0
            
            for k in range(i+1, len(nums)):
                curr = nums[i]
                
                if nums[k] > nums[i]:
                    curr  += dfs(k, dp)
                    
                maximum = max(maximum, curr)   
            
            dp[i] = maximum
            return dp[i]
        
        dp = { n-1: nums[n-1] }
        maximum = 0
        for i in range(len(nums)):
            curr = dfs(i, dp)
            maximum = max(curr, maximum)

            
        return maximum
    
print(maxSumIS([44, 47, 32, 22, 26], 5))