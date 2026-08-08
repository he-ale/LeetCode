from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next= head
        aux= temp
        while aux.next:
            if aux.next.val==val:
                aux.next= aux.next.next
            else:
                aux= aux.next
        return temp.next
