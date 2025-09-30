from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Linked List Cycle Detection
        Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
        There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer
        """
        if not head or not head.next:
            return False

        slow_pointer = head
        fast_pointer = head.next

        # while fast pointer isn't at the end of the list
        # run the tortoise-hare procedure
        while fast_pointer:
            if slow_pointer == fast_pointer:
                return True

            # advance slow pointer by 1 node
            slow_pointer = slow_pointer.next
            # advance fast pointer by 2 nodes, safely
            if fast_pointer.next and fast_pointer.next.next:
                fast_pointer = fast_pointer.next.next
            else:
                # Reached end of list, no cycle
                return False
        # If loop finishes without finding a cycle (shouldn't happen with the logic above,
        # but included for completeness or alternative implementations)
        return False
