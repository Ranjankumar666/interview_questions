def isUpPossible(i,j , arr, visited):
    return i - 1 > -1 and  visited.get(f'{i-1},{j}') is None

def isDownPossible(i, j, arr, visited):
    return i + 1 < len(arr) and  visited.get(f'{i+1},{j}') is None

def isLeftPossible(i, j, arr, visited):
    return j - 1 > -1 and visited.get(f'{i},{j-1}') is None

def isRightPossible(i, j, arr, visited):
    return j + 1 < len(arr[0]) and visited.get(f'{i},{j+1}') is None

def traverse(i, j , arr, res, visited):

    res.append(arr[i][j])
    visited[f'{i},{j}'] = True
    
    if isUpPossible(i, j, arr, visited):
        visited[f'{i-1},{j}'] = True
        return traverse(i-1, j , arr,res, visited)

    elif isRightPossible(i, j, arr, visited):
        visited[f'{i},{j+1}'] = True 
        return traverse(i, j+1, arr, res, visited)

    elif isDownPossible(i, j, arr, visited):
        visited[f'{i+1},{j}'] = True
        return traverse(i+1, j , arr, res, visited)

    elif isLeftPossible(i, j, arr, visited):
        visited[f'{i},{j-1}'] = True 
        return traverse(i, j-1, arr, res, visited)
    
    return res

def DFS(arr):
    visited = {}
    res = []

    return traverse(0, 0,arr, res , visited)

arr = [range(1,6), range(6, 11), range(11, 16), range(16, 21)]
# print(DFS(arr))
