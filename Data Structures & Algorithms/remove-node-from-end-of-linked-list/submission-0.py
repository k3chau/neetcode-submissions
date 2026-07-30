# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        D = ListNode()
        D.next = head
        A = B = D
        for _ in range(n+1): 
            A = A.next
        while A:
            A = A.next
            B = B.next
        B.next = B.next.next
        return D.next
        