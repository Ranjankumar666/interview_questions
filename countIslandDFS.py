from collections import deque
from typing import Tuple


def visitIslands(mat, i, j):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque[Tuple[int, int]]()
    r = len(mat)
    c = len(mat[0])
    count = 0

    queue.append((i, j))
    while len(queue) > 0:
        i, j = queue.popleft()
        count += 1
        for d in dirs:
            p = i + d[0]
            q = j + d[1]

            if -1 < p < r and -1 < q < c and mat[p][q] == 1:
                queue.append((p,q))

        mat[i][j] = 0

    return count

def countIslands(mat):
    r = len(mat)
    c = len(mat[0])
    count = 0

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                count += 1 
                visitIslands(mat, i, j)
    
    return count

mat = [[0, 1],[1, 0], [1, 1], [1, 0]]

print(countIslands(mat))
