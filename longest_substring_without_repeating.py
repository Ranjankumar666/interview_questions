
from itertools import count


def bruteForce(S: str) -> int:

    max_count = 0
        
    n = len(S)
    
    if n <= 1:
        return n 

    count = 0
    
    for i in range(n):
        mp = {}
        curr_count = 0  
        count += 1

        for j in range(i, n):
            count += 1
            if S[j] not in mp:
                mp[S[j]] = True
                curr_count += 1

                if max_count < curr_count:
                    max_count = curr_count
            else:
                break
    
    print(count)
    return max_count


def solution(S: str) -> int:
    mp = {}
    count = 0

    i  = 0
    n = len(S)
    max_l = 0
    curr_l = 0

    while i < n:
        count += 1

        if mp.get(S[i]) is None:
            mp[S[i]] = i
            curr_l += 1
            i += 1
           
        else:
            # start next to where it is found
            i = mp[S[i]] + 1
            if max_l <= curr_l:
                max_l = curr_l
            curr_l = 0
            mp = {}

    if max_l <= curr_l:
            max_l = curr_l

    print(count)
    return max_l

##Optimal
def solution2(S):

    mp = {}
    
    i  = 0
    j = 0
    n = len(S)
    max_l = 0
    count = 0
    

    while j < n:
        count += 1
        if mp.get(S[j]) is None or i > mp[S[j]] :
            mp[S[j]] = j
            j += 1   
        else:
            i = mp[S[j]] + 1

        max_l = max(max_l, (j - i))

    print(count)
    return max_l

def getSubStrings(S):
    n = len(S)
    
    left = 0
    res = []
    mp = {}
    
    for right in range(n):
        currChar = S[right]
        isPresent = mp.get(S[right])
        
        if isPresent is None or left > isPresent:
            mp[currChar] = right
        else:
            res.append(S[left: right+1])
            left = isPresent + 1
           
        
    return res
    
            
        
testStr = "ABCDGH"
# print(solution2(testStr), solution(testStr))
print(getSubStrings(testStr))