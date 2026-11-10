# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head

        while fast and fast.next: # slow is at middle when fast reaches the end
            slow = slow.next
            fast = fast.next.next
        
        curr = slow # second half starts at slow
        prev = None
        while curr is not None: # reverse the second half
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        while prev.next is not None: # connect both lists
            head_nxt = head.next # save head.next
            prev_nxt = prev.next # save prev.next
            head.next = prev # link node in the 1st half to the 2nd half
            prev.next = head_nxt # link node in the 2nd half to the 1st half
            head = head_nxt # advance in 1st half
            prev = prev_nxt # advance in 2nd half
        