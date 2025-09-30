import pytest
from typing import Optional, List as PyList # Use PyList to avoid conflict with ListNode
from prac.MergeTwoSortedLists import Solution, ListNode

solution = Solution()

def list_to_nodes(items: PyList[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def nodes_to_list(node: Optional[ListNode]) -> PyList[int]:
    items = []
    while node:
        items.append(node.val)
        node = node.next
    return items

def test_both_empty():
    l1 = list_to_nodes([])
    l2 = list_to_nodes([])
    merged = solution.mergeTwoLists(l1, l2)
    assert nodes_to_list(merged) == []

def test_one_empty():
    l1 = list_to_nodes([1, 2, 4])
    l2 = list_to_nodes([])
    merged = solution.mergeTwoLists(l1, l2)
    assert nodes_to_list(merged) == [1, 2, 4]

    l1_empty = list_to_nodes([])
    l2_full = list_to_nodes([1, 3, 4])
    merged2 = solution.mergeTwoLists(l1_empty, l2_full)
    assert nodes_to_list(merged2) == [1, 3, 4]

def test_notebook_example():
    l1_nodes = list_to_nodes([0, 2])
    l2_nodes = list_to_nodes([1, 3])
    merged = solution.mergeTwoLists(l1_nodes, l2_nodes)
    assert nodes_to_list(merged) == [0, 1, 2, 3]

def test_interleaved():
    l1 = list_to_nodes([1, 5, 10])
    l2 = list_to_nodes([2, 3, 12])
    merged = solution.mergeTwoLists(l1, l2)
    assert nodes_to_list(merged) == [1, 2, 3, 5, 10, 12]

def test_with_duplicates():
    l1 = list_to_nodes([1, 1, 5])
    l2 = list_to_nodes([1, 2, 6])
    merged = solution.mergeTwoLists(l1, l2)
    assert nodes_to_list(merged) == [1, 1, 1, 2, 5, 6]
