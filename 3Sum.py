class Solution:
    # Hashmap ver
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hm = collections.defaultdict(list)
        a = list()
        for i in range(n):
            for j in range(i+1, n):
                hm[nums[i]+nums[j]].append([i,j])
        
        for i in range(n):
            if -nums[i] in hm:
                for h in hm[-nums[i]]:
                    
                    [j,k] = h
                    if i != j and i != k:
                        a.append(sorted([nums[i], nums[j], nums[k]]))
        
        # Remove duplicate triplets
        b = list()
        for sublist in a:
            if sublist not in b:
                b.append(sublist)
        return b

    # Two pointer ver
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        a = list()
        for k in range(n):
            i,j = k+1, n-1
            while i<j:
                s = nums[i]+nums[j]
                if s == -nums[k]:
                    a.append((nums[k],nums[i], nums[j]))
                    i+=1
                    j-=1
                elif s > -nums[k]:
                    j-=1
                else:
                    i+=1
        
        # Remove duplicate triplets
        b = list()
        for sublist in a:
            if sublist not in b:
                b.append(sublist)
        return b