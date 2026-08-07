from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux= head
        size= 0
        while aux:
            size+=1
            aux= aux.next

        if (n == size):
            head= head.next if head.next else None
            return head

        n= size-n
        aux2= head
        while (n > 1):
            n-=1
            aux2= aux2.next

        if aux2.next and aux2.next.next:
            aux2.next= aux2.next.next
        else:
            aux2.next= None
        return head

        if aux2.next and aux2.next.next:
            aux2.next= aux2.next.next
        else:
            aux2.next= None
        return head