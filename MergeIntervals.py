class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        rslt = []
        if len(intervals) == 0:
            return rslt
        
        intervals.sort()
        start_x, start_y = intervals[0]
        
        for i in range(1, len(intervals)):
            if start_y < intervals[i][0]:
                rslt.append([start_x, start_y])
                start_x, start_y = intervals[i]
            elif start_y < intervals[i][1]:
                start_y = intervals[i][1]
                
        rslt.append([start_x, start_y])
        return rslt
                