class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
	    
        def recursive(start:int, arr:[]):
            if start == len(nums):
                return
            
            output.append(arr[:])
            for i in range(start+1, len(nums)):
                
                arr.append(nums[i])
                recursive(i, arr)
                arr.pop()
                
        recursive(-1, [])
            
        return output

        