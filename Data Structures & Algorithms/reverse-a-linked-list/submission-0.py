# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr =[]
        if(curr is None):
            return head
        while(curr.next):
            arr.append(curr.val)
            curr = curr.next
        head = curr
        while(arr):
            curr.next = ListNode(arr.pop())
            curr = curr.next
        return head
        