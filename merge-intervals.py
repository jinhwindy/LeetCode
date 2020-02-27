class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length=len(intervals)
        if length<2:
            return intervals
        result=[]
        intervals.sort()
        i=0
        while i<length:
            left=intervals[i][0]
            right=intervals[i][1]
            i+=1
            while i<length and right>=intervals[i][0]:
                right=max(intervals[i][1],right)
                i+=1
            result.append([left,right])
        return result
