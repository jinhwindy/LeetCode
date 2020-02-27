class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAr=0
        j=len(height)-1
        i=0
        while i<j:
            Area=min(height[i],height[j])*(j-i)
            if Area>maxAr:
                maxAr=Area
            if height[i]<height[j]:
                i+=1
            else:
                j=j-1
        
        return maxAr
