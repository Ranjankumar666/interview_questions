def celebrity(mat):
    n = len(mat)
    
    candidate = 0
    
    for j in range( n):
        # Get the potential candidate
        if mat[candidate][j] == 1:
            candidate = j
            
            
    # verify the celebrity
    for k in range(n):
        if candidate == k:
            continue
        
        if mat[candidate][k] == 0 and mat[k][candidate] == 1: 
            continue

        return -1
    
    
    return candidate
            
print(celebrity([
    [0, 1, 1 ,1],
    [0, 0, 0, 0],
    [1, 1, 0, 0], 
    [ 1, 1, 0, 0]
]))
