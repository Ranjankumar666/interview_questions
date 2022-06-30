def isPalid(s):
    return s == s[::-1]

def palindromePartition(s):

    res = []
    curr = []
    
    def dfs(i):
        if i >= len(s):
            res.append(curr[:])
            return
        
        for j in range(i, len(s)):
            s1 = s[i:j+1]
            if isPalid(s1):
                curr.append(s1)
                
                dfs(j+1)
                
                curr.pop()
                
    
    dfs(0)
    
    return res
        
            
        
print(palindromePartition('aab'))