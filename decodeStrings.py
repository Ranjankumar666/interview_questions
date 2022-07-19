letters = {str(i - 64): chr(i) for i in range(65, 91) }


def solution(s, i, dp):
    if i in dp: return dp[i]
    
    if s[i] == '0':
        return 0

    
    count = 0
    
    count += solution(s, i+1, dp) 
    
    if i +1 < len(s) and s[i] + s[i+1]  in letters:
        count += solution(s , i+2, dp)
    
    
    dp[i] = count
    return count
    
s = '11106'
print(solution(s, 0, { len(s) : 1 }))
        