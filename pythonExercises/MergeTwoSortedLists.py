from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listMergued= ListNode(0)
        aux= listMergued

        while list1 and list2:
            if (list1.val > list2.val):
                aux.next= ListNode(list2.val)
                list2= list2.next
            else: 
                aux.next= ListNode(list1.val)
                list1= list1.next
            aux= aux.next

        while list1:
            aux.next= ListNode(list1.val)
            aux= aux.next
            list1= list1.next

        while list2:
            aux.next= ListNode(list2.val)
            aux= aux.next
            list2= list2.next

        return listMergued.next

s= Solution()

s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))) , ListNode(1, ListNode(3, ListNode(4))))
