import pytest
from typing import Optional
from MaxDepthBinaryTree import Solution, TreeNode

solution = Solution()

def test_empty_tree():
    assert solution.maxDepth(None) == 0

def test_single_node_tree():
    root = TreeNode(1)
    assert solution.maxDepth(root) == 1

def test_simple_tree():
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert solution.maxDepth(root) == 3

def test_left_skewed_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert solution.maxDepth(root) == 4

def test_right_skewed_tree():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert solution.maxDepth(root) == 4
