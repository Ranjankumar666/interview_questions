def maxProductSubArray(arr):
    prodArr = [-float('inf'), 0]


    def solution(arr, start, end):
        if len(arr) <= 0:
            return 1

        if len(arr) == 1:
            return arr[0]

        left = arr[start: end]
        right = arr[end:]

        prod  = solution(left, start, end-1)*solution(right, end, end)

        if prod > prodArr[0]:
            prodArr[0] = prod
            prodArr[1] = end - start + 1
        
        
        return prod

    solution(arr, 0 , len(arr) )

    return prodArr[1]


arr = [6 , -3, -10, 0 , 2 ]
print(maxProductSubArray(arr))