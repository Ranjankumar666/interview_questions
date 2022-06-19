from collections import deque


dirs = [ (-1, 0), (0, 1), (1, 0), (0, -1)]

def inRange(p, q, grid):
    N = len(grid)
    M = len(grid[0])

    return -1 < p < N and -1 < q < M

def traverse(i, j, grid):
    q = deque()
    q.append((i, j))
    visited = [[False for j in i] for i in grid]

    while len(q) > 0:
        i, j = q.popleft()
        visited[i][j] = True

        if grid[i][j] == 2:
            return True

        for adj in dirs:
            a, b = adj

            a += i
            b += j
            
            if inRange(a, b, grid) and not visited[a][b] and grid[a][b] != 0:
                q.append((a, b))

    return False

def pathExists(grid):
    N = len(grid)
    M = len(grid[0])


    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                return traverse(i, j, grid) 

grid = [
    [3 ,0 ,3 ,0 ,0], 
    [3 ,0 ,0 ,0 ,3], 
    [3 ,3 ,3, 3 ,3 ],
    [0 ,2 ,3 ,0 ,0 ],
    [3 ,0 ,3 ,1 ,3]
]

# grid = [[1 ,3], [3, 2]]

print(pathExists(grid))