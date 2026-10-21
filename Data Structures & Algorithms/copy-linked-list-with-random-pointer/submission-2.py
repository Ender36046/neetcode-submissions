"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head == None):
            return None
        if(head.next == None):
            if(head.random != None):
                tempNode = Node(head.val, None, None)
                tempNode.random = tempNode
                return tempNode
            return Node(head.val, None, None)
        hashmap = {}
        curr = head.next
        deepHead = Node(head.val)
        deepCurr = deepHead
        hashmap[head] = deepHead
        while(curr != None):
            deepCurr.next = Node(curr.val)
            deepCurr = deepCurr.next
            hashmap[curr] = deepCurr
            curr = curr.next

        curr = head
        deepCurr = deepHead
        while(curr != None):
            if(curr.random == None):
                deepCurr.random = None
            else:
                randNode = hashmap[curr.random]
                deepCurr.random = randNode

            curr = curr.next
            deepCurr = deepCurr.next

        return deepHead