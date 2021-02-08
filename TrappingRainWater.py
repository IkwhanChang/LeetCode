class Solution:
    def trap(self, height: List[int]) -> int:
        highest_left, highest_right = [0], [0]
        n = len(height)
        
        for i in range(1, n):
            highest_left.append(max(highest_left[i-1], height[i-1]))
            highest_right.append(max(highest_right[i-1], height[n-i]))
        
        
        t = 0
        for i in range(1,n-1):
            w = min(highest_left[i], highest_right[n-i]) - height[i]
            t += 0 if w<0 else w
        return t