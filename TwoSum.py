class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target, a = target - b
        # first insert all target - b in map valued as index no
        # second, find if a exist in b if not equal index
        
        d = collections.defaultdict(int)
        for i, num in enumerate(nums):
            d[target - num] = i
            
        for i, num in enumerate(nums):
            if num in d and d[num] != i:
                return [i, d[num]]
        return []