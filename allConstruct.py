def prefix(a, b):
    if  len(b) > len(a): return 
    
    n = len(b)
    
    for i in range(n):
        if a[i] != b[i]:
            return 
        
    return a[n: ]

def allConstruct( target, words, dp={}):
    if target in dp: dp[target]
    if target == '': return [[]]
    
    allways = []
    for word in words:
        suffix = prefix(target, word)
        
        if  suffix is not None:
            res = allConstruct(suffix, words, dp)
            targetWays = list(map(lambda x: [word] + x , res))
            
            allways = allways + targetWays
                
    dp[target] = allways
        
    return allways


# print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
