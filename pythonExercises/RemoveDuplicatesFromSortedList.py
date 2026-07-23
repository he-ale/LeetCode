from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional[ListNode]=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result= aux = ListNode(head.val)
        currentValue= head.val
        while head.next:
            head= head.next
            if(head.val!=currentValue):
                aux.next= ListNode(head.val)
                currentValue= head.val
                aux= aux.next
        return result

s= Solution()
a= s.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))

while a:
    print(a.val, sep=" ")
    a= a.next