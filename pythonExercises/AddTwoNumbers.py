from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result= ListNode()
        current= result
        carry= False

        while (l1 is not None and l2 is not None):
            aux= l1.val+l2.val
            if carry:
                aux+=1
            
            if(aux>9):
                carry= True
                current.next= ListNode(aux%10)
            else:
                carry= False
                current.next= ListNode(aux)

            l1= l1.next
            l2= l2.next
            current= current.next

        while (l1 is not None):
            if carry:
                l1.val+=1
            
            if(l1.val>9):
                carry= True
                current.next= ListNode(l1.val%10)
            else:
                carry= False
                current.next= ListNode(l1.val)

            l1= l1.next
            current= current.next

        while (l2 is not None):
            if carry:
                l2.val+=1
            
            if(l2.val>9):
                carry= True
                current.next= ListNode(l2.val%10)
            else:
                carry= False
                current.next= ListNode(l2.val)

            l2= l2.next
            current= current.next

        if carry:
            current.next= ListNode(1)

        return result.next