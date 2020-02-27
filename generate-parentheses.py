class Solution:
    def func(self,collection:List[str],s:str,left:int,right:int,n:int):
        if left<right or left>n or right>n:
            return
        if left==n and right==n:
            collection.append(s)
            return
        self.func(collection,s+'(',left+1,right,n)
        self.func(collection,s+')',left,right+1,n)
        return

    def generateParenthesis(self, n: int) -> List[str]:
        collection=[]
        s=''
        left=0
        right=0
        self.func(collection,s,left,right,n)
        return collection
