from typing import List


def minPathSum( grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        directions = [
            (1, 0),
            (0, 1)
        ]
        
        
        for r in range(M):
            for c in range(N):
                
                mini = float('inf')
                
                if(r-1 >= 0):
                    mini = min(mini, grid[r-1][c])
                   
                if(c-1 >= 0):
                    mini = min(mini,  grid[r][c-1])

                if( mini != float('inf')):
                    grid[r][c] += mini

        

        return grid[M-1][N-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1, 3], [1, 5]]))