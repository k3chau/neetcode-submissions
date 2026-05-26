# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0 
        ans = []
        dummyNode = ListNode(0)
        while curr1 or curr2:
            sumNode = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
            lastDigit = sumNode % 10
            carry = sumNode // 10
            ans.append(lastDigit)
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        if carry:
            ans.append(carry)
        cur = dummyNode
        for i in range(len(ans)):
            cur.next = ListNode(ans[i])
            cur = cur.next
        return dummyNode.next


        