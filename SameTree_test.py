import pytest
from typing import Optional
from SameTree import Solution, TreeNode

solution = Solution()

def test_both_none():
    assert solution.isSameTree(None, None) == True

def test_one_none():
    p = TreeNode(1)
    assert solution.isSameTree(p, None) == False
    assert solution.isSameTree(None, p) == False

def test_same_single_node():
    p = TreeNode(1)
    q = TreeNode(1)
    assert solution.isSameTree(p, q) == True

def test_different_single_node():
    p = TreeNode(1)
    q = TreeNode(2)
    assert solution.isSameTree(p, q) == False

def test_same_tree_structure():
    # p =   1      q =   1
    #      / \          / \
    #     2   3        2   3
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert solution.isSameTree(p, q) == True

def test_different_tree_structure_val():
    # p =   1      q =   1
    #      / \          / \
    #     2   3        2   4
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(4))
    assert solution.isSameTree(p, q) == False

def test_different_tree_structure_shape():
    # p =   1      q =   1
    #      /            / \
    #     2            2   3
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert solution.isSameTree(p, q) == False

def test_from_notebook_example():
    p = TreeNode(1)
    q = TreeNode(1)
    assert solution.isSameTree(p, q) == True
