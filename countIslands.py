def checkIsland(i, j, mat, r, c):
    mat[i][j] = '0'
    directions = [(1, 0), (0, 1), (-1, 0), [0, -1]]
    
    for d in directions:
        p = i + d[0]
        q = j + d[1]
        
        if -1 < p < r and -1 < q < c and mat[p][q] == '1':
            checkIsland(p, q, mat, r, c)


    return 
    

def countIslands(mat, r,c ):
    count = 0
    
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '1': 
                checkIsland(i, j, mat, r, c)
                count += 1

    return count

mat = [[0, 1,],[1, 0], [1, 1], [1, 0]]

print(countIslands(mat, len(mat), len(mat[0])))