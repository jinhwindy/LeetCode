class Solution:
    def bisearch(self,nums: List[int], target: int,begin:int,end:int) -> int:
        if end-begin==0:
            if nums[begin]!=target:
                return -1
            else :
                return 0+begin
        '''
        将数组一分为二，
        其中一定有一个是有序的(开头小于结尾，则有序)，
        另一个可能是有序，也能是部分有序。
        此时有序部分用二分法查找。
        无序部分再一分为二，其中一个一定有序，
        另一个可能有序，可能无序。就这样循环.
        '''
        i=0+begin
        j=end
        if nums[i]==target:
            return i
        if nums[j]==target:
            return j
        
        mid=(i+j)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>nums[i]:
            # 有序:二分法
            if target>nums[mid] or target<nums[i]:
                pass
            else :
                begin=i
                end=mid
                while begin<=end:
                    middle=(begin+end)//2
                    if nums[middle]==target:
                        return middle
                    elif nums[middle]>target:
                        end=mid-1
                    else :
                        begin=mid+1
        else:
            # 无序：递归调用
            result1=self.bisearch(nums,target,i,mid)
            if result1!=-1:
                return result1
        # //////////////////////////////////////////////////
        if nums[mid]<nums[j]:
            # 有序:二分法
            if target<nums[mid] or target>nums[j]:
                pass
            else :
                begin=mid
                end=j
                while begin<=end:
                    middle=(begin+end)//2
                    if nums[middle]==target:
                        return middle
                    elif nums[middle]>target:
                        end=middle-1
                    else:
                        begin=middle+1
        else:
            # 无序：递归调用
            result=self.bisearch(nums,target,mid,j)
            if result!=-1:
                return result
        if result1==-1 and result==-1:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if length==0:
            return -1
        if length==1:
            if nums[0]!=target:
                return -1
            else :
                return 0
        result=self.bisearch(nums,target,0,len(nums)-1)
        return result
