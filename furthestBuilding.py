def furthest(heights, bricks, ladders, i, dp):
        
    if dp[i] is not None: return dp[i]
    if i == len(heights) - 1:
        return i 
    
    
    if bricks <= 0 and ladders <= 0:
        if heights[i+1] <= heights[i]: 
            return furthest(heights, bricks, ladders, i+1,dp)
        
        return i - 1

    if heights[i+1] <= heights[i]: 
        return furthest(heights, bricks, ladders, i+1,dp)
    
    if bricks <= 0:
        return furthest(heights, 0, ladders - 1, i + 1, dp)
    
    diff = 0
    if bricks > 0:
        diff = (heights[i+1] - heights[i])
        
    if ladders <= 0:
        return furthest(heights, bricks - diff, 0 , i + 1 , dp)
   
    return  max(
            furthest(heights, bricks - diff, ladders , i+1, dp),
            furthest(heights, bricks, ladders - 1 , i + 1, dp),
        ) 
            
            
    
    
print(furthest([4, 2], 0, 0, 0, [None]*2))
print(furthest([4,2,7, 10],
5,
1, 0, [None]*7
))
    