import pytest
from typing import List
from prac.BinarySearchProblem import Solution

solver = Solution() # Renamed from 'b' in notebook for clarity

def test_notebook_example():
    assert solver.search([-1,0,2,4,6,8],4) == 3

def test_target_found_start():
    assert solver.search([1,2,3,4,5], 1) == 0

def test_target_found_end():
    assert solver.search([1,2,3,4,5], 5) == 4

def test_target_not_found():
    assert solver.search([1,2,3,4,5], 6) == -1

def test_empty_list():
    assert solver.search([], 1) == -1

def test_single_element_found():
    assert solver.search([5], 5) == 0

def test_single_element_not_found():
    assert solver.search([5], 1) == -1
