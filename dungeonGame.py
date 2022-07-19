def calculateMinimumHP(grid):
    M = len(grid)
    N = len(grid[0])
    
    table = [[abs(grid[i][j]) for j in range(N)] for i in range(M)]

    
    for r in range(M):
        for c in range(N):
            
            mini = float('inf')
            
            if(r-1 >= 0):
                mini = min(mini, abs(table[r-1][c]))
                
            if(c-1 >= 0):
                mini = min(mini,  abs(table[r][c-1]))

            if( mini != float('inf')):
                table[r][c] += mini
                path.append(mini)

    
    print(path)
    return table[M-1][N-1]

print(calculateMinimumHP([[1], [-2], [1]]));
print(calculateMinimumHP([[-3, 5]]));
print(calculateMinimumHP([[100]]));
print(
	calculateMinimumHP([
		[-2, -3, 3],
		[-5, -10, 1],
		[10, 30, -5],
	])
);
print(
	calculateMinimumHP([
		[1, -3, 3],
		[0, -2, 0],
		[-3, -3, -3],
	])
);