def isPalindrome(s, i, j):
    mid = i + (j -1)//2
    p = mid 
    q = mid
    

    
    while p >= i and q < j:
            if s[i] != s[j]: return False
            
            i -= 1
            j += 1
            
    return True


def longestPalindrome(S,i , j, dp={}):
    

    if (i, j) in dp:
        return dp[(i , j)]
    
    if (j - i) == 1:
        return (i , j)
    
    if isPalindrome(S, i , j):
        dp[(i, j)] = (i, j) 
        return dp[(i , j)]
    

    d = longestPalindrome(S, i+1, j, dp)
    b = longestPalindrome(S, i, j-1,  dp)
    
    longest = (-1,-1)
    
    if b[1] - b[0] > longest[1] - longest[0]: longest = b
    if d[1] - d[0] > longest[1] - longest[0]: longest = d
        
    
    dp[(i , j)] = longest
    return longest


def driver(s):
    i , j = longestPalindrome(s ,0 , len(s),  {})
    return s[i:j]


def longestPalindromeOptimal(s):
    
    def expand(i, j):
        
        while i >= 0 and j < len(s)   and s[i] == s[j]:
            i -= 1
            j += 1
        
        return s[i+1: j]
    
    longest = ''
    for i in range(len(s)):
        s1 = expand(i, i)
        s2 = expand(i, i+1)
        
        if len(s1) > len(longest): longest = s1
        if len(s2) > len(longest): longest = s2


    return longest     

                
print(longestPalindromeOptimal('cbbd'))
# print(longestPalindromeOptimal('abcdaa'))
# print(longestPalindromeOptimal('findnitianhere'))