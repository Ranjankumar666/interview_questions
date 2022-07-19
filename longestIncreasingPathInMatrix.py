from typing import List

def longestIncreasingPath( matrix: List[List[int]]) -> int:
    M =  len(matrix)
    N = len(matrix[0])
    
    directions = [
        (-1, 0),
        (0, 1), 
        (1, 0),
        (0, -1)
    ]
    
    
    dp = {}
    
    def dfs(i, j):
        if (i,j) in dp: return dp[(i, j)]
        if i >= M or j >= N or i < 0 or j < 0:
            return 0
        
        
        maxPath = 1
        
        for d in directions:
            p,q = d
            p, q = i+p, j+q
            
            if p >= M or q >= N or p < 0 or q < 0 :
                continue
                
            if matrix[p][q] > matrix[i][j]:
                path = 1 +  dfs(p, q)
                maxPath = max(path, maxPath)
                
                
        dp[(i,j)] = maxPath
        return maxPath
    
    
    maxi = 0
    
    
    for i in range(M):
        for j in range(N):
            path = dfs(i, j)
            maxi = max(path, maxi)
            
    return maxi


print(longestIncreasingPath([[1, 2]]))