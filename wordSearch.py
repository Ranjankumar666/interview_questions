directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def searchWord(mat, word, i=0, j=0, k=0, visited= {}):
        
    if (i,j) in visited:
        return False
    
    if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 :
        return False
    
    if k == len(word):
        return True

    if mat[i][j] != word[k]:
        return False
    

    

    
    visited[(i,j)] = True
    
    for d in directions:
        p,q = d
        if searchWord(mat, word, i+p, j+q , k+1, visited):
            return True
    
    return False


mat = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(searchWord(mat, word))

mat = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(searchWord(mat, word))

                
