
def localMax( arr , i):

    if i == 0:
        return arr[0]

    local = max(arr[i], arr[i] +  localMax(arr, i-1))


    return max(local, 0)

    

def maxSubArraySum(arr, N):
    return localMax(arr, N-1)

arr = [-1, -2, -3, -4]
N = len(arr)
print(maxSubArraySum(arr, N))
