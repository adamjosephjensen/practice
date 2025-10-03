# test_character_replacement.py
import random
import string
import pytest

from prac.LongestRepeatingCharacterReplacement import Solution

@pytest.fixture
def solution():
    return Solution()

def oracle_bruteforce(s: str, k: int) -> int:
    # O(n^2 * Σ) oracle (incremental freq), fine for n<=200
    n = len(s)
    best = 0
    for i in range(n):
        freq = {c: 0 for c in string.ascii_uppercase}
        max_same = 0
        for j in range(i, n):
            ch = s[j]
            freq[ch] += 1
            if freq[ch] > max_same:
                max_same = freq[ch]
            span = j - i + 1
            need = span - max_same
            if need <= k and span > best:
                best = span
    return best

# 1) known/edge cases (explicitly target the 3 “off by …” bugs)
@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("ABAB", 2, 4),          # baseline
        ("AABABBA", 1, 4),       # lc classic
        ("", 0, 0),              # empty
        ("A", 0, 1),             # single
        ("AAAA", 0, 4),          # all same
        ("ABCD", 1, 2),          # no repeats, small k
        ("ABCDEF", 10, 6),       # k >= len(s) ⇒ whole string
        ("ABBB", 2, 4),          # =k exactly
        ("BAAAB", 2, 5),         # best ends at rr == n (catches n+1)
        ("AABBBCC", 0, 3),       # longest run with k=0
        ("ABAB", 0, 1),          # alternating w/ k=0
        ("ZAZAZ", 2, 5),         # Z-heavy → catches ord('A') mistakes
        ("AZZZY", 1, 4),         # need == k boundary
    ],
)
def test_known_cases(solution, s, k, expected):
    assert solution.characterReplacement(s, k) == expected

# 2) properties
@pytest.mark.parametrize("s", [
    "", "A", "AB", "BAAAB", "ABABABAB", "ZZZZ", "QWERTYUIOPASDFGHJKLZXCVBNM",
])
@pytest.mark.parametrize("k", [0, 1, 2, 5, 100])
def test_bounds_and_k0_property(solution, s, k):
    ans = solution.characterReplacement(s, k)
    assert 0 <= ans <= len(s)
    if k == 0:
        # longest consecutive run
        best = 0; cur = 0; prev = None
        for ch in s:
            cur = cur + 1 if ch == prev else 1
            prev = ch
            best = max(best, cur)
        assert ans == best

def test_monotone_in_k(solution):
    s = "AABABBAZXYZ"
    vals = [solution.characterReplacement(s, k) for k in range(0, 6)]
    assert all(vals[i] <= vals[i+1] for i in range(len(vals) - 1))

def test_relabel_invariance(solution):
    rnd = random.Random(7)
    s = "".join(rnd.choice("ABCDE") for _ in range(30))
    k = 3
    ans = solution.characterReplacement(s, k)
    # random permutation of letters in alphabet used
    mapping = dict(zip("ABCDE", rnd.sample("ABCDE", 5)))
    t = "".join(mapping[ch] for ch in s)
    assert solution.characterReplacement(t, k) == ans

# 3) random small vs oracle (fuzz)
@pytest.mark.parametrize("alphabet, n, trials, max_k", [
    ("AB", 12, 250, 6),
    ("ABCDE", 10, 250, 4),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 8, 250, 4),
])
def test_random_small_against_oracle(solution, alphabet, n, trials, max_k):
    rnd = random.Random(1337)
    for _ in range(trials):
        length = rnd.randint(0, n)
        s = "".join(rnd.choice(alphabet) for _ in range(length))
        k = rnd.randint(0, min(max_k, length))
        expect = oracle_bruteforce(s, k)
        got = solution.characterReplacement(s, k)
        assert got == expect, f"s={s!r}, k={k}, expect={expect}, got={got}"

# 4) pathological shapes
def test_pathological_blocks(solution):
    # alternating prefix + big C block → best window soaks with exact k
    s = "AB" * 20 + "CCCCCCC"  # length 47
    assert solution.characterReplacement(s, 3) == 10

