#User function Template for python3
def isInRange(num, start, end):
    if num is None:
        return False
        
    if num >= start and num <= end:
        return True
    
    return False
    
def isInt(num):
    try :
        l = int(num)
        return l
    except:
        return None
        
def leadingZeros(s):
    if s == '0':
        return 0
    
    return len(s) - len(s.lstrip('0'))

    
def isValid(s):
    #code here
    arr = s.split('.')
        
    if len(arr) != 4:
        return False
        
    
        
    for i in arr:
        if len(i) > 3:
            return False

        if(leadingZeros(i) > 0):
            return False
            
        l = isInt(i)
        if i is None:
            return False
            
        inRange = isInRange(l, 0 , 255)
        
        if inRange == False:
            return False
            
    return True

print(isValid('00.00.00.00'))