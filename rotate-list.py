# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        work=head
        pri=head
        length=0
        while work!=None:
            work=work.next
            length+=1
        if length==0:
            return 
        if length==0 or head.next==None or k%length==0:
            return head
        work=head
        # 第一步：将链连接为一个环
        # 将环按需打断
        for i in range(length-1):
            work=work.next
        work.next=head
        work=head
        for i in range(length-k%length-1):
            work=work.next
        pri=work.next
        work.next=None
        return pri
        # for j in range(k%length):
        #     i=0
        #     while i<length-2:
        #         work=work.next
        #         i+=1
        #     pri=work.next
        #     work.next=pri.next
        #     pri.next=head
        #     work=pri
        # return head
