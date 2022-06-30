def prefix(a, b):
    if  len(b) > len(a): return 
    for i in range(len(b)):
        if a[i] != b[i]:
            return None
        
    return a[len(b):]


def canConstruct(target, arr, dp ={}):
    
    if target in dp: return dp[target]
    if target == '': return True
    
    for i in arr:
        
        r = prefix(target, i)
        
        if r is not None and canConstruct(r, arr):
            dp[target] = True
            return True
    
    dp[target] = False    
    return False


def canConstructTable(target, arr):
    N = len(target)
    table = [False for _ in range(N + 1)]
    
    table[0] = True
    
    for i in range( N + 1):
        if table[i]:
            curr = target[i: ]
            for j in arr:
                if prefix(target[i:], j) is not None:
                    if i + len(j) < N + 1:
                        table[i + len(j)] = True
    
    print(table)
    return table[N]

def allConstruct(target, arr):
    N = len(target)
    table = [[] for _ in range(N + 1)]
    
    table[0] = [[]]
    
    for i in range( N + 1 ):
        if len(table[i]) != 0:
            curr = target[i:]
            for j in arr:
                if prefix(curr, j) is not None:
                    if i + len(j) < N + 1:
                        res = list(map(lambda x: x + [j], table[i]))
                        table[i + len(j)] += res
    

    return table[N]
        
# print(
#     canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])
# )

# print(canConstruct('isamsung', 'i like sam sun samsung mobile ice cream icecream man go mango'.split(' ')))

# print(canConstructTable('isamsung', 'i like sam sun samsung mobile ice cream icecream man go mango'.split(' ')))

print(canConstructTable('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
# print(canConstructTable('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
#m: length of target; n: length of words array
#Brute Force: O(n^m*m)