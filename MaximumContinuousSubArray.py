class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum_so_far = 0
        rslt = -10**5
        
        for num in nums:
            
            sum_so_far = max(sum_so_far + num, num)
            rslt = max(rslt, sum_so_far)
        return rslt