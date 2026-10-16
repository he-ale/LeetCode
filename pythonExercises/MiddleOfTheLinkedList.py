# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        ls= []
        while head:
            ls.append(head.val)
            head= head.next

        index= (len(ls)//2)
        middle= ListNode(0)
        aux= middle
        for e in ls[index:]:
            aux.next= ListNode(e)
            aux= aux.next
        return middle.next