# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head==None:
            return None
        def findMidNode(tempHead,tempEnd):
            if tempEnd==None:
                print("head: %d and end :None"%tempHead.val)
            else:
                print("head: %d   end: %d"%(head.val,tempEnd.val))
            if tempHead==tempEnd:
                return None
            elif tempHead.next==tempEnd:
                return tempHead
            slowPoint=tempHead.next
            prePoint=tempHead.next.next
            while slowPoint!=tempEnd and prePoint!=tempEnd:
                if prePoint.next!=tempEnd:
                    prePoint=prePoint.next.next
                else:
                    return slowPoint
                slowPoint=slowPoint.next
            return slowPoint
        def buildTree(head,end):
            if head==None:
                return
            rootNode=findMidNode(head,end)
            if rootNode==None:
                return None
            else:
                root=TreeNode(rootNode.val)
                root.left=buildTree(head,rootNode)
                root.right=buildTree(rootNode.next,end)
            return root
        return buildTree(head,None)
