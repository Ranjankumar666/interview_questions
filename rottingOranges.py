def solution(arr):
    N = len(arr)
    M = len(arr[0])

    freshCount = 0
    rotten = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                freshCount += 1
            elif arr[i][j] == 2:
                rotten.append((i,j))


    