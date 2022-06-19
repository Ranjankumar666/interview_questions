def convertToArray(x: str): return list(map(int, x.split(' ')))

def solution(arr, n):
    
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    #maximum reach at current position
    maxReach = arr[0]
    #minimum jumos
    jumps = 1
    #steps left for current position
    steps = arr[0]
    
    for i in range(1, n):
        if i == n-1:
            return jumps

        maxReach = max(maxReach, i + arr[i])
        
        steps -= 1
        
        if steps == 0:
            jumps += 1
            
            if i >= maxReach:
                return -1
            
            steps = maxReach - 1
    
    return jumps

arr = convertToArray('1 3 5 8 9 2 6 7 6 8 9')
memo = [None]*len(arr)
print(solution(arr, len(arr)))