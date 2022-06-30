from collections import Counter

def isGoodString(s):
    if s == '':
        return True
    
    count = Counter(s)
    
    for i in count.keys():
        if count[i] != '' and count[i] > 1:
            return False
    
    return True
    

def goodString(string, i, dp = {}):
    
    key = (string, i)
    
    
    if key in dp: dp[key]
    
    if isGoodString(string):
        return 1
    
    if i == 0  and isGoodString(string) is False :
        return float('inf')


    shortest = float('inf')
    t1 = 0
    t2 = 0
    
    t1 += goodString(string[:i-1] + string[i:], i -1)
    t2 += goodString(string, i - 1 )
    res = min(t1, t2)
    
    shortest=  min(shortest, res)
        
    dp[key] = shortest
    
    return shortest
    

print(goodString('abbabaab', 8))
print(goodString('aabc', 4))
print(goodString('aaaaa', 5))