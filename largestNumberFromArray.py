
    
def largestNumber(curr, arr, i):
    if i >= len(arr) - 1:
        return curr
    
    if curr != '':
        t1 = curr + str(arr[i+1])
        t2 = str(arr[i+1]) + curr
        
        curr = str(max(int(t1), int(t2)))
    else:
        curr = str(arr[i+1])
        
    return largestNumber(curr, arr, i+1)

if __name__ == '__main__':
            
    print(largestNumber('', [83, 9 ,1, 94], -1))
    print(largestNumber('', [3, 30, 34, 5, 9], -1))
    print(largestNumber('', [54, 546, 548, 60], -1))
            
