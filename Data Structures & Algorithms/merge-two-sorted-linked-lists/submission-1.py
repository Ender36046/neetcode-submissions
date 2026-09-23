# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        head = newList

        while(list1 != None or list2 != None):
            if(list1 == None):
                newList.next = list2
                break
            elif(list2 == None):
                newList.next = list1
                break
            if(list1.val >= list2.val):
                newList.next = list2
                list2 = list2.next
            else:
                newList.next = list1
                list1 = list1.next
            newList = newList.next
        return head.next
        