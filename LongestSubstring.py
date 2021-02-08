class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #"pwwkew"
        if len(s) == 0:
            return 0
        n = len(s)
        d = collections.defaultdict(int)
        prev_j, longest_substr = 0,0
        
        for i in range(0,n): 
            
            if s[i] in d:
                prev_j = max(prev_j, d[s[i]]+1)
            d[s[i]] = i
                
            longest_substr = max(i - prev_j + 1, longest_substr)
        return longest_substr