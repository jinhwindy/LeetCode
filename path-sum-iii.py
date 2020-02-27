class Solution:
    def findSum(self, tempRoot,rootToNow,sum):
            if tempRoot==None:
                return 0
            tempSum=tempRoot.val
            if tempSum==sum:
                n=1
            else:
                n=0
            for i in range(len(rootToNow)-1,-1,-1):
                tempSum+=rootToNow[i]
                if tempSum==sum:
                    n+=1
            right=self.findSum(tempRoot.right,rootToNow+[tempRoot.val],sum)
            left=self.findSum(tempRoot.left,rootToNow+[tempRoot.val],sum)
            return left+right+n
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return  self.findSum(root,[],sum)
