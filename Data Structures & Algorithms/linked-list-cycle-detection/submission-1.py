# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None or head.next == None):
            return False
        node1 = head.next
        node2 = head
        while(node1 != None and node2 != None):
            if(node1 == node2):
                return True
            for i in range(2):
                if(node1 == None):
                    return False
                node1 = node1.next
            node2 = node2.next
        return False