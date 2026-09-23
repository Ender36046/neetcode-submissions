# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        nextNode = head.next
        previousNode = None
        while(nextNode != None):
            nextNode = head.next
            head.next = previousNode
            previousNode = head
            if(nextNode != None):
                head = nextNode
            
        return head
        