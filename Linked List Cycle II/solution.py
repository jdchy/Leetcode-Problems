# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        n = head
        while n.next != None:
            if n.val != "&M#^a":
                n.val = "&M#^a"
                n = n.next
            else:
                return n