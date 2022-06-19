import sys


INF = float('inf')
dirs = [(-1, 0), (0, 1), (1, 0), (0,-1)]


def dfs(i, j, grid, steps,  N, M):
    if i < 0 or j < 0 or i >= N or j >= M:
        return

    if steps > grid[i][j]:
        return

    steps += 1
    if steps < grid[i][j]:
        grid[i][j] = steps

    for d in dirs:
        dfs(i + d[0], j +d[1],grid,  steps, N ,M)


def solution(grid):
    N = len(grid)
    M = len(grid[0])

    gates = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0 :
                gates.append((i, j))

    
    for gate in gates:
        i, j = gate 
        dfs(i, j , grid, -1, N, M)
                

    return grid

grid = [
    [INF, -1, 0, INF], 
    [-1, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]              

print(solution(grid))