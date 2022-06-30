def validCombs(curr ,k,  words, dp={}):
    N = len(curr)
    
    
    if N == 3:
        return 1
    
    if (curr, k) in dp: 
        return dp[(curr, k)]
    
    count = 0
    
    i = k + 1
    while i < (len(words)):
        w = words[i]
        
        if curr[N-1] != w:
            count += validCombs(curr + w, i , words, dp)
        i += 1
            
    dp[(curr, k)] = count       
    return count

def nonConsectives(s):

    
    count = 0
    dp = {}
    for i in range(len(s)):

            count += validCombs(s[i] ,i ,  s, dp)
    
    return count


print(nonConsectives("001101"))
print(nonConsectives("0001100100"))