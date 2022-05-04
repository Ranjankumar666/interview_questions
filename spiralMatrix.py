keygen = lambda i,j : f'{i},{j}'

def spiralTraverse(mat,r, c):
    
    visited = {}
    res = []

    p, q = 0, 0 
    while p < r/2 and q < c/2:
        i,j = p, q

        while j < c:
            key = keygen(i, j)
            if visited.get(key) is None:
                visited[key] = True
                res.append(mat[i][j])
                j += 1
            else:
                break
        i += 1
        j -= 1

        while i < r:
            key = keygen(i, j)
            if visited.get(key) is None:
                visited[key] = True
                res.append(mat[i][j])
                i += 1
            else:
                break
        j -= 1
        i -= 1

        while j > -1:
            key = keygen(i, j)
            if visited.get(key) is None:
                visited[key] = True
                res.append(mat[i][j])
                j -= 1
            else:
                break

        i -= 1
        j += 1

        while i > -1:
            key = keygen(i, j)
            if visited.get(key) is None:
                visited[key] = True
                res.append(mat[i][j])
                i -= 1
            else:
                break
        
        p += 1
        q += 1
    
    return res

def spiralTraverse2(mat,r, c, k):
    
    visited = {}

    res = []
    count = 0

    p, q = 0, 0 
    while p < r/2 and q < c/2:
        i,j = p, q

        while j < c:

            if not visited.get((i, j)) :
                visited[i, j] = True
                res.append(mat[i][j])
                j += 1
                count += 1
            else:
                break
            
            if count > k:
                return res[k-1]
            

        i += 1
        j -= 1

        while i < r:

            if not visited.get((i, j)) :
                visited[i, j] = True
                res.append(mat[i][j])
                i += 1
                count += 1
            else:
                break
            
            if count > k:
                return res[k-1]
        j -= 1
        i -= 1

        while j > -1:

            if not visited.get((i, j)) :
                visited[i, j] = True
                res.append(mat[i][j])
                j -= 1
                count += 1
            else:
                break
            
            if count > k:
                return res[k-1]

        i -= 1
        j += 1

        while i > -1:
 
            if not visited.get((i, j)) :
                visited[i, j] = True
                res.append(mat[i][j])
                i -= 1
                count += 1
            else:
                break
            if count > k:
                return res[k-1]
        
        p += 1
        q += 1
    
    print(res)
    return res[k-1]

mat = [[1 ,2 , 3 ],[4 ,5 ,6], [7, 8, 9]]
print(spiralTraverse2(mat, len(mat), len(mat[0]), 4))