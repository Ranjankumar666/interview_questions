def jumpGame(arr):
    n = len(arr)
    table = [False for _ in range(n)]
    
    table[0] = True
    
    for i in range(n):
        if table[i]:
            for j in range(1, arr[i]+1):
                if i + j <  n:
                    table[i + j] = True
                else:
                    return True
                    
    return table[n-1]


print(jumpGame([2 ,3,1, 1, 4]))
print(jumpGame([3,2,1,0,4]))