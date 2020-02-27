# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[]
        res=[]
        temp=root
        rear=None
        while len(stack) or temp!=None:
            if temp!=None:
                while temp:
                    stack.append(temp)
                    temp=temp.left
            else:
                temp=stack[len(stack)-1]
                # 当temp.right==None时，当前节点无右子树，则可以访问该节点本身
                # 当temp.right==None时，右子树已经访问过，则可以访问该节点本身
                if temp.right==None or temp.right==rear:
                    res.append(temp.val)
                    rear=temp
                    del stack[len(stack)-1]
                    # 将temp赋值为None是为了在下一次while循环中跳转到else中获得stack的栈顶
                    temp=None
                else:
                    temp=temp.right
        return res
