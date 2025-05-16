import pytest
from typing import Optional, List # Add List for create_linked_list values
from cycle_detection import Solution, ListNode

# Helper function to create a linked list from a list of values
# and optionally create a cycle by connecting the tail to the node at pos index.
def create_linked_list(values: List[int], pos: int = -1) -> Optional[ListNode]:
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
    assert not solution.hasCycle(head) # Expected: False


def test_multiple_nodes_no_cycle():
    """Tests a list with multiple nodes and no cycle."""
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4])
    assert not solution.hasCycle(head) # Expected: False


def test_list_with_cycle():
    """Tests a list where the tail connects back to an earlier node."""
    solution = Solution()
    head = create_linked_list([3, 2, 0, -4], pos=1) # Cycle: -4 -> 2
    assert solution.hasCycle(head) # Expected: True


def test_cycle_at_head():
    """Tests a list where the tail connects back to the head."""
    solution = Solution()
    head = create_linked_list([1, 2], pos=0) # Cycle: 2 -> 1
    assert solution.hasCycle(head) # Expected: True


def test_single_node_cycle():
    """Tests a list with a single node pointing to itself."""
    solution = Solution()
    head = create_linked_list([1], pos=0) # Cycle: 1 -> 1
    assert solution.hasCycle(head) # Expected: True
