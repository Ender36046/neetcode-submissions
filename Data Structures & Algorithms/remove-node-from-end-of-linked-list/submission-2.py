# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        countNode = head
        while(countNode != None):
            count+=1
            countNode = countNode.next

        newN = count - n

        if(newN == 0):
            nextNode = head.next
            head = None
            return nextNode

        nodeBeforeDelete = head
        for i in range(newN-1):
            nodeBeforeDelete = nodeBeforeDelete.next

        deletedNode = nodeBeforeDelete.next
        nodeBeforeDelete.next = deletedNode.next

        return head