class Solution:
    def rob(self, root: TreeNode) -> int:
        def postrob(cur):
            if cur==None:
                return [0,0]
            res=[]
            # res[0]表示不打劫当前节点
            # res[1]表示打劫当前节点
            l=postrob(cur.left)
            r=postrob(cur.right)
            res.append(max(l[0],l[1])+max(r[0],r[1]))
            res.append(l[0]+r[0]+cur.val)
            return res
        if root==None:
            return 0
        res=postrob(root)
        return max(res[0],res[1])
