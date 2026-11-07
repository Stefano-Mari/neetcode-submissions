# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # create a placeholder node
        curr = dummy # set curr to placeholder node

        while list1 and list2: # while both lists still have values
            if list1.val <= list2.val:
                curr.next = list1 # attach list1 node to merged list
                list1 = list1.next # get next list1 node
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next # move tail to node just attached

        curr.next = list1 if list1 else list2 # attach leftover nodes
        return dummy.next # return everything past dummy node