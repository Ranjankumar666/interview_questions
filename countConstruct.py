def prefix(a, b):
    if  len(b) > len(a): return 
    
    n = len(b)
    
    for i in range(n):
        if a[i] != b[i]:
            return 
        
    return a[n: ]

def countConstruct( target, words, dp= {}):
    if target in dp: return dp[target]
    if target == '': return 1
    
    count  = 0
    for word in words:
        suffix = prefix(target, word)
        
        if  suffix is not None:
            count += countConstruct(suffix, words)
        
    dp[target] = count 
    return count



def countConstructTable(target, words):
    N = len(target)
    table = [0 for i in range(N + 1)]
    
    table[0] = 1
    
    for i in range(N+1):
        
        if table[i] != 0:
            curr = target[i:]
            for word in words:
                suffix = prefix(curr, word)
                
                if suffix is not None and i + len(word) < N+1:
                    table[i + len(word)] += table[i]
                    
    print(table)
    return table[N]
            
# print(
#     countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])
# )

# print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
# print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

print(countConstructTable('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstructTable('purple', ['purp', 'p', 'ur', 'le', 'purpl']))