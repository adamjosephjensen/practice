# test_check_inclusion.py
# run: pytest -q

import pytest

from PermutationInString import Solution  # adjust if your module name differs


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        # examples from prompt
        ("abc", "lecabee", True),
        ("abc", "lecaabee", False),
        # basics
        ("ab", "eidbaooo", True),     # "...baoo..." -> "ba" is a perm
        ("ab", "eidboaoo", False),    # classic negative
        ("abc", "abc", True),         # exact match
        ("abc", "zzzabcyyy", True),   # direct substring
        ("abcd", "abc", False),       # s1 longer than s2
        # repeats / counts
        ("aab", "aaab", True),        # "...aaab" -> "aab" present
        ("aab", "aba", True),         # "aba" contains a perm of "aab"
        ("aab", "aaa", False),        # counts off (need a 'b')
        ("aaa", "baaac", True),       # run of same char
        # edges at boundaries
        ("abc", "xxabcyy", True),     # at start/middle
        ("abc", "yycabxx", True),     # at start after rotation
        # multiple windows
        ("ab", "abxaba", True),       # several valid windows
        # empties (convention: empty s1 -> True, empty s2 only True if s1 empty)
        ("", "anything", True),
        ("", "", True),
        ("a", "", False),
    ],
)
def test_check_inclusion_parametrized(s1, s2, expected):
    sol = Solution()
    assert sol.checkInclusion(s1, s2) is expected


def test_no_side_effects_on_inputs():
    # strings are immutable, but we assert anyway for paranoia
    sol = Solution()
    s1 = "ab"
    s2 = "zzabzz"
    _ = sol.checkInclusion(s1, s2)
    assert s1 == "ab"
    assert s2 == "zzabzz"
