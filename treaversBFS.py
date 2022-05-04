from collections import deque

from DFSmatrix import isDownPossible, isLeftPossible, isRightPossible, isUpPossible

def BFS(arr, start=(0, 0)):
    visited = {}
    res = []

    q = deque()

    q.append(start)
    

    while len(q) > 0:
        (i, j) = q.popleft()
        res.append(arr[i][j])
        visited[f'{i},{j}'] = True

        if isUpPossible(i, j, arr, visited): 
            visited[f'{i-1},{j}'] = True
            q.append((i-1, j))

        
        if isRightPossible(i, j, arr, visited): 
            visited[f'{i},{j+1}'] = True 
            q.append((i, j+1))

        if isDownPossible(i, j, arr, visited):
            visited[f'{i+1},{j}'] = True 
            q.append((i+1, j))

        if isLeftPossible(i, j, arr, visited): 
            visited[f'{i},{j-1}'] = True 
            q.append((i, j-1))

    
    return res

arr = [range(1,6), range(6, 11), range(11, 16), range(16, 21)]
print(BFS(arr, start=(2, 2)))