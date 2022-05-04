def maxLength(arr):

    mp = {}
    cumSum = 0
    maxLen = 0

    for i in range(len(arr)):
        cumSum += arr[i]

        if cumSum == 0: maxLen = max(maxLen, i + 1)
        elif mp.get(cumSum) is not None: maxLen(maxLen, abs(i - mp[cumSum]))
        else: mp[cumSum] = i
    
    return cumSum