# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        prev = 10001
        t = 0
        if not head:
            return None
        while head:
            if prev == head.val:
                head = head.next
                continue
            prev = head.val
            node.val = head.val
            head = head.next
            node.next = ListNode()
            t = node
            node = node.next
        t.next = None
        return dummy