# tests/MinStack_test.py
import pytest
from prac.MinStack import Solution

@pytest.fixture
def S():
    return Solution()

cases = [
        # ops, args, expected returns (None for void), note
    (["push","push","push","getMin","pop","top","getMin"],
     [   [3],   [5],   [2],     [],   [],   [],     [] ],
     [  None,  None,  None,      2,  None,    5,      3],
     "min tracks down then up"),
    (["push","push","push","getMin","push","getMin"],
     [   [2],   [2],   [2],     [],   [1],     [] ],
     [  None,  None,  None,      2,  None,      1],
     "duplicates ok"),
    (["push","top","getMin","push","getMin","pop","getMin"],
     [   [-1],  [],     [],      [-2],  [],   [],     [] ],
     [   None, -1,     -1,       None,  -2,  None,    -1],
     "negatives"),
    ]

@pytest.mark.parametrize("ops,args,rets,_", cases, ids=[c[-1] for c in cases])
def test_sequences(ops, args, rets, _, S):
    for op, a, expect in zip(ops, args, rets):
        got = getattr(S, op)(*a)
        assert got == expect

def test_min_is_monotone_nonincreasing_on_pushes_of_new_mins(S):
    seq = [5,4,4,3,10,3,2,2]
    mins = []
    for v in seq:
        S.push(v)
        mins.append(S.getMin())
    # each min <= previous min
    assert all(b <= a for a,b in zip(mins, mins[1:]))

def test_min_restores_after_popping_to_prev_min(S):
    for v in [5, 1, 3]:
        S.push(v)
    assert S.getMin() == 1
    S.pop()            # pop 3
    assert S.getMin() == 1
    S.pop()            # pop 1
    assert S.getMin() == 5

def test_underflow_raises_on_top_and_getMin_and_pop(S):
    with pytest.raises(IndexError):
        S.top()
    with pytest.raises(IndexError):
        S.getMin()
    with pytest.raises(IndexError):
        S.pop()
