# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = ListNode(0)
        res = val
        ex = 0
        while l1 or l2 or ex:
            if l1:
                ex += l1.val
                l1 = l1.next
            if l2:
                ex += l2.val
                l2 = l2.next
        
            res.next = ListNode(ex%10)
            res = res.next
            ex = ex//10
        
        return val.next