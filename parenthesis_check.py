def isPair(a ,b):
    try:
        ob = ['{', '(', '[']
        cb = ['}', ')', ']']
        
        o1 = ob.index(a)
        o2 = cb.index(b)
        return o1 == o2
        
    except ValueError:
        return False
def isOB(x):
    try:
        ob = ['{', '(', '[']
        o1 = ob.index(x)
        
        return True
        
    except ValueError:
        return False

def isCB(x):
    try:
        cb = ['}', ')', ']']
        o1 = cb.index(x)
        
        return True
        
    except ValueError:
        return False

def ispar(x):
    # code here
    
    n = len(x)
        
    if n <= 1:
        return False
        
    stk = []
    
    for i  in x:
        if isOB(i):
            stk.append(i)
        else:
            try:
                top = stk.pop()
                
                if isPair( top, i) is False:
                    return False
            except IndexError:
                return False
    
    if len(stk) == 0:
        return True
    
    return False


print(ispar('{([])}'))