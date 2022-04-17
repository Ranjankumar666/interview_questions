#Brute Force 
def solution_v1(arr):
    n = len(arr)

    for i in range(n):
        curr_sum = arr[i]

        for j in range(i+1, n):
            curr_sum += arr[j]
            target = -curr_sum

            if target in arr[j+1:]:
                return True
            
            curr_sum -= arr[j]
    
    return False

#N^2
def solution(arr, p):
    n = len(arr)
    

    for i in range(n):
        curr_sum = arr[i]
        mp = {}
        k = p-curr_sum

        for j in range(i+1, n):
            if mp.get(arr[j]):
                return True
            else:
                mp[k - arr[j]] = j
            
    return False

print(solution([1, 4, 45, 6, 10, 8], 13))