class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        
        i = 0
        j = 1
        
        curr = s[i]
        longest = 0
        
        while i <= j and j < len(s):
            if s[j] not in  curr:
                    curr += s[j]
                    j+= 1
            else:
                longest = max(len(curr), longest)
                i = i +1
                curr = s[i]
                j = i+1
                
        return max(curr, longest)
    

print(Solution().lengthOfLongestSubstring('au'))


    