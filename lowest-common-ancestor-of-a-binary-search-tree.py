class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        result=root
        def findComAnce(tempRoot,p,q):
            nonlocal result
            if (tempRoot.val-p.val)*(tempRoot.val-q.val)<=0:
                result=tempRoot
            elif (tempRoot.val-p.val)>0 and (tempRoot.val-q.val)>0:
                findComAnce(tempRoot.left,p,q)
            else:
                findComAnce(tempRoot.right,p,q)
        findComAnce(root,p,q)
        return result
