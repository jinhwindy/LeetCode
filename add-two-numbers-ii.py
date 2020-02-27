# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        def add(num1, num2, i, j):
            if not i or not j:
                return 0
            if num1 > num2:
                temp = i.val + add(num1 - 1, num2, i.next, j)
            else:
                temp = i.val + j.val + add(num1, num2, i.next, j.next)
            i.val = temp % 10
            return temp // 10

        num1 = num2 = 0
        cur = l2
        while cur:
            num2 += 1
            cur = cur.next
        cur = l1
        while cur:
            num1 += 1
            cur = cur.next
        
        if num2 > num1:
            l1, l2 = l2, l1
            num2, num1 = num1, num2

        if add(num1,num2,l1, l2):
            l2 = ListNode(1)
            l2.next = l1
            l1 = l2
        return l1

# 作者：alice-37
# 链接：https://leetcode-cn.com/problems/add-two-numbers-ii/solution/python-di-gui-zhi-xing-yong-shi-52-ms-zai-suo-you-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
