# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1 = ""
        tmp1 = l1
        v2 = ""
        tmp2 = l2
        while tmp1: 
            v1 += str(tmp1.val)
            tmp1 = tmp1.next
        
        while tmp2:
            v2 += str(tmp2.val)
            tmp2 = tmp2.next
        
        head = ListNode()
        ans = head
        v1 = int(v1[::-1])
        v2 = int(v2[::-1])
        tmp = v1+v2
        while tmp:
            target = tmp % 10
            ans.val = target
            tmp //= 10
            if not tmp:
                break
            ans.next = ListNode()
            ans = ans.next
        print(v1, v2)
        return head
        