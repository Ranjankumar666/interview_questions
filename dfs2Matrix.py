dirs = [(-1, 0), (0, 1), (1, 0), (0,-1)]

def inRange(i, j, grid):
    N = len(grid)
    M = len(grid[0])

    return -1 < i < N and -1 < j < M

def dfs(i, j, grid, visited, res):
    if not inRange(i, j, grid):
        return 
    
    visited[i][j] = True
    res.append(grid[i][j])
    for d in dirs:
        p, q = d
        p += i
        q += j

        if inRange(p, q, grid) and not visited[p][q]:
            dfs(p, q, grid, visited, res)
    

def traverse(grid):
    visited = [ [False for i in row] for row in grid]  
    res = [] 
    dfs(0, 0, grid, visited, res)

    return res


grid = [[1 ,2, 3, 4], [5 ,6 , 7, 8], [9 , 10, 11, 12]]

print(traverse(grid))


    
