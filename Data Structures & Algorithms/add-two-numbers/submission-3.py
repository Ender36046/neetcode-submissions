# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1 = l1
        currl2 = l2
        result = ListNode(0, None)
        head = result
        carryOver = 0

        while(currl1 != None or currl2 != None):
            addl1 = 0
            addl2 = 0
            if(currl1 != None):
                addl1 = currl1.val

            if(currl2 != None):
                addl2 = currl2.val
            result.val = addl1 + addl2 + carryOver
            if(result.val > 9):
                carryOver = 1
                result.val -= 10
            else:
                carryOver = 0

            if(currl1 != None):
                currl1 = currl1.next
            if(currl2 != None):
                currl2 = currl2.next
            if(currl1 != None or currl2 != None):
                result.next = ListNode(0,None)
                result = result.next

        if(carryOver):
            result.next = ListNode(1,None)

        return head
            


        