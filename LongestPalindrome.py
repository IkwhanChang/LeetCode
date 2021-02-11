class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def maxPalindrome(s: str, i: int, j: int) -> str:
            if s[i] != s[j]:
                return ""
            c = s[i] if i==j else s[i]+s[j]
            i-=1
            j+=1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                c = s[i] + c + s[j]
                i-=1
                j+=1
                
            return c
        
        m,r = 0, ""
        for i in range(0, len(s)-1):
                ss = maxPalindrome(s, i, i)
            
                if len(ss) > m:
                    m = len(ss)
                    r = ss
                    
                ss = maxPalindrome(s, i, i+1)
            
                if len(ss) > m:
                    m = len(ss)
                    r = ss

        return r
            
            