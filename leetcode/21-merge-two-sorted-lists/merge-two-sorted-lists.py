# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        tmp = answer
        if not list1 and not list2:
            answer.val = []
            return 
        while list1  or list2:
            if not list1  and list2:
                if not tmp.val:
                    tmp.val = list2.val
                    tmp.next = list2.next
                else:
                    tmp.next = list2
                break
            elif not list2 and list1:
                if not tmp.val:
                    tmp.val = list1.val
                    tmp.next = list1.next
                else:
                    tmp.next = list1
                print(answer, tmp)
                break
            if list1.val < list2.val:
                tmp.val = list1.val
                list1 = list1.next
            elif list2.val <= list1.val:
                tmp.val = list2.val
                list2 = list2.next
            tmp.next = ListNode()
            tmp = tmp.next


        return answer 