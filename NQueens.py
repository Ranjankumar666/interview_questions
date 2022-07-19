from operator import truediv


def NQueen(N):
    res = []
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [['.']*N for i in range(N)]

    
    def dfs(r):

        if r == N:
            res.append([''.join(row) for row in  board])
            return 
        
        
        for c in range(N):
            if (c in cols or (r+c) in pos_diag or (r-c) in neg_diag):
                continue
            
            cols.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            
            board[r][c] = 'Q'
            dfs(r+1)
            
            board[r][c] = '.'

            cols.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
        
        return res
            

    dfs(0)
                
    return res


print(NQueen(4))