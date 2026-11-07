# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # slow pointer
        fast = head # fast pointer

        while fast and fast.next: 
            slow = slow.next # move 1 at a time
            fast = fast.next.next # move 2 at a time

            if slow == fast: # if they meet, cycle exists
                return True

        return False # if they don't meet, no cycle exists