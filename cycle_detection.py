from typing import Optional
import pytest

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
            # advance slow pointer by 2 nodes, safely
            if fast_pointer.next and fast.pointer.next.next:
                fast_pointer = fast_pointer.next.next
            else:
                return False


# Helper function to create a linked list from a list of values
# and optionally create a cycle by connecting the tail to the node at pos index.
def create_linked_list(values: list, pos: int = -1) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    if pos != -1 and pos < len(nodes):
        current.next = nodes[pos]  # Create cycle
    return head

# --- Test Cases ---

def test_empty_list():
    """Tests an empty list (head is None)."""
    solution = Solution()
    head = create_linked_list([])
    assert not solution.hasCycle(head) # Expected: False


def test_single_node_no_cycle():
    """Tests a list with a single node and no cycle."""
    solution = Solution()
    head = create_linked_list([1])
    # assert not solution.hasCycle(head) # Expected: False
    with pytest.raises(NotImplementedError):
         solution.hasCycle(head)


def test_multiple_nodes_no_cycle():
    """Tests a list with multiple nodes and no cycle."""
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4])
    # assert not solution.hasCycle(head) # Expected: False
    with pytest.raises(NotImplementedError):
         solution.hasCycle(head)


def test_list_with_cycle():
    """Tests a list where the tail connects back to an earlier node."""
    solution = Solution()
    head = create_linked_list([3, 2, 0, -4], pos=1) # Cycle: -4 -> 2
    # assert solution.hasCycle(head) # Expected: True
    with pytest.raises(NotImplementedError):
         solution.hasCycle(head)


def test_cycle_at_head():
    """Tests a list where the tail connects back to the head."""
    solution = Solution()
    head = create_linked_list([1, 2], pos=0) # Cycle: 2 -> 1
    # assert solution.hasCycle(head) # Expected: True
    with pytest.raises(NotImplementedError):
         solution.hasCycle(head)


def test_single_node_cycle():
    """Tests a list with a single node pointing to itself."""
    solution = Solution()
    head = create_linked_list([1], pos=0) # Cycle: 1 -> 1
    # assert solution.hasCycle(head) # Expected: True
    with pytest.raises(NotImplementedError):
         solution.hasCycle(head)
