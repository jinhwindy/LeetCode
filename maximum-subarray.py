class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        result=nums[0]
        temp=0
        '''
        假设sum<=0，那么后面的子序列肯定不包含目前的子序列，
        所以令sum = num；如果sum > 0对于后面的子序列是有好处的。
        res = Math.max(res, sum)保证可以找到最大的子序和。
        '''
        for i in range(len(nums)):
            if temp>0:
                temp+=nums[i]
            else:
                temp=nums[i]
            if temp>result:
                result=temp
        return result
