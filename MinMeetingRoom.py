class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        A = [i for [i,j] in sorted(intervals, key=lambda a: a[0])]
        B = [j for [i,j] in sorted(intervals, key=lambda a: a[1])]
        
        s = 0
        i,j = 0,0
        m = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                s+=1
                i+=1
            else:
                s-=1
                j+=1
            m = max(m,s)
        
        return m