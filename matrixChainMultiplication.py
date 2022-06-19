def solution(arr):
    if len(arr) == 1:
        return arr[0]

    # if len(arr) == 2:
    #     return arr[0]*arr[1]
    # if len(arr) == 3:
    #     return arr[0]*arr[1]*arr[2]

    
    a = arr[0]*arr[1]*solution(arr[2:])
    b = solution(arr[:-2])
  
    return min(a, b)


arr = [10,30, 5, 60]
print(solution(arr))