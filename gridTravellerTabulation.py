def gridTravellerTabulation(m , n):
    table = [[0 for i in range(n+1)] for j in range(m+1)]
    
    
    table[1][1] = 1
    
    for i in range(m+1):
        for j in range(n+1):
            if j+1 < n + 1:
                table[i][j+1] += table[i][j]
            if i+1 < m + 1:
                table[i + 1][j] += table[i][j]
                
    return table[m][n]

def gridTraveller( grid):
    m = len(grid)
    n = len(grid[0])
    
    grid[0][0] = 10
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            
            d = i + 1
            r = j + 1
            
            if d < m and grid[d][j] != 1:
                grid[d][j] += grid[i][j]
            
            if r < n and grid[i][r] != 1:
                grid[i][r] += grid[i][j]
                
    
    return grid[m-1][n-1]//10

# print(gridTravellerTabulation(3 ,3))
# print(gridTravellerTabulation(18 ,18))

print(gridTraveller([[0,0,0],[0,1,0],[0,0,0]]))