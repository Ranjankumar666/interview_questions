def setZeros(mat):
    m = len(mat)
    n = len(mat[0])
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                
                if mat[i][0] == 'y':
                    mat[i][0] = 'yx'
                
                if mat[m-1][j] == 'x' or mat[m-1][j] == 'y':
                    mat[m-1][j] = 'xy'
                else:
                    mat[m-1][j] = 'y'
                    
    
    print(mat)
    
    for col in range(n):
        if mat[m-1][col] == 'y':
            
            for row in range(m):
                mat[row][col] = 0
        
        elif mat[m-1][col] == 'xy':
            mat[m-1] = [0]*n
            for row in range(m):
                mat[row][col] = 0
                
                      
    for row in range(m):
        if mat[row][0] == 'x':
            mat[row] = [0]*n
        
        elif mat[row][0] == 'xy':
            mat[row] = [0]*n
            for col in range(n):
                mat[row][col] = 0
            
            



                
    return mat

# print(setZeros([[1,1,1],[1,0,1],[1,1,1]]))
# print(setZeros( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
# print(setZeros([[1],[0]]))
# print(setZeros([[0, 1]]))
print(setZeros([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))