phoneDict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'ijk',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'xyz'
}



def soln(s):
    res = []
    
    def dfs(curr, i):
        if len(curr) == len(s):
            res.append(curr)
            return 
        
        if s[i] in  phoneDict:
            p = phoneDict[s[i]]
            
            for k in p:
                curr = curr + k
                dfs(curr, i+1)
                
                curr = curr[:-1]
                
    
   
    dfs('', 0)
        
    
    return res

print(soln('23'))
  
        
                