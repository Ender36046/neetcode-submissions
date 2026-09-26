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

    def reorderList(self, head: Optional[ListNode]) -> None:
        currNode = head
        count = 0
        countNode = head
        while(countNode != None):
            countNode = countNode.next
            count+=1

        countNode = head
        for i in range(math.ceil(count/2)):
            countNode = countNode.next

        splitNode = head
        for i in range(math.ceil(count/2)-1):
            splitNode = splitNode.next

        splitNode.next = None
            

        reverse = self.reverseList(countNode)
        while(reverse != None):
            nextNode = currNode.next
            prevNode = reverse.next

            currNode.next = reverse
            reverse.next = nextNode

            reverse = prevNode
            currNode = nextNode