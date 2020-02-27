class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length=len(nums)
        if length<2:
            return True

        # 不断拓展最大能到达的位置
        # 贪心算法
        maxreach=0
        stand=0
        for i in range(length-1):
            # ////////////////////////////
            if i>maxreach:
                return False
            # ////////////////////////////
            maxreach=max(maxreach,i+nums[i])
            if maxreach>=length-1:
                return True
        return False
