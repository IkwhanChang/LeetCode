class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1]*(n+1)
        
        for i in range(1,n):
            prod[i] = prod[i-1] * nums[i-1]
            
        mul_sofar = 1
        for i in range(n,0,-1):
            prod[i-1] *= mul_sofar
            mul_sofar *= nums[i-1]
            
            
        return prod[:-1]