# ------------------------------------------------------------
# Find the element with odd occurrence (XOR method)
# ------------------------------------------------------------
# Logic:
# XOR has useful properties:
# 1. x ^ x = 0
# 2. x ^ 0 = x
# 3. XOR is commutative and associative
#
# So, when we XOR all elements:
# - Even-occurring numbers cancel out
# - The odd-occurring number remains
#
# Example:
# arr = [1, 2, 3, 2, 3, 1, 3]
# Stepwise XOR:
# 1 ^ 2 ^ 3 ^ 2 ^ 3 ^ 1 ^ 3
# → (1^1) ^ (2^2) ^ (3^3) ^ 3
# → 0 ^ 0 ^ 0 ^ 3 = 3
# ------------------------------------------------------------

from typing import List


def one_odd_occuring(arr: List[int]) -> int:
    res = 0
    for item in arr:
        res ^= item  # ✅ fix here
    return res


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
tests = [
    ([1, 2, 3, 2, 3, 1, 3], 3),
    ([4, 4, 5, 5, 6], 6),
    ([10], 10),
    ([7, 7, 8], 8),
    ([2, 2, 2], 2),
]


# ------------------------------------------------------------
# Run Tests
# ------------------------------------------------------------
if __name__ == "__main__":
    for arr, expected in tests:
        result = one_odd_occuring(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} one_odd_occuring({arr}) = {result}")
