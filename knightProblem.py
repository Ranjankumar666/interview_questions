D = [
    (-2, 1),
    (-2, -1),
    (2, 1),
    (2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2)
]

def isInRange(N, r, c):
    if -1 < r < N and -1 < c < N:
        return True

    return False



def visit(N , k, r, c, dp):

    if k == 0  :
        return 1

    if dp[r][c] and k == dp[r][c][1]:
        return dp[r][c][0]

    curr = 0
    for d in D:
        p = r + d[0]
        q = c + d[1]

        if isInRange(N, p, q):
            a = visit(N , k-1, p, q, dp)
            curr += a/8

    
  
    dp[r][c] = (curr, k)


    return curr

N = 8
dp = [ [False for i in range(N)] for j in range(N) ]        
k = 30
print(visit(N, k, 6, 4, dp))
