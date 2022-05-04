from itertools import count


def visitIslands(mat, i, j,r, c):
    mat[i][j] = 0
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for d in directions:
        p = i + d[0]
        q = j + d[1]

        if -1 < p < r and -1 < q < c and mat[p][q] == '1':
            visitIslands(mat, p, q , r, c)


def countIslands(mat):
    r = len(mat)
    c = len(mat[0])
    count = 0
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                visitIslands(mat, i, j , r, c)
                count += 1
    
    return count