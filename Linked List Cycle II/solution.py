<<<<<<< HEAD
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
=======
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
>>>>>>> b05c634ed04fe1f6b8ce602691e720e7f248e177
                return n