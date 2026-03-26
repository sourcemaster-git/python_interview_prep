# ------------------------------------------------------------
# Check if a number is a power of 2
# ------------------------------------------------------------
# Logic:
# A power of 2 has exactly ONE set bit.
#
# Example:
# 1  -> 0001
# 2  -> 0010
# 4  -> 0100
# 8  -> 1000
#
# Property:
# n & (n - 1) == 0  → only true for powers of 2
#
# But we must also ensure n > 0
# ------------------------------------------------------------


def isPower2(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
tests = [
    (0, False),
    (1, True),
    (2, True),
    (3, False),
    (4, True),
    (5, False),
    (8, True),
    (16, True),
    (18, False),
]


# ------------------------------------------------------------
# Run Tests
# ------------------------------------------------------------
if __name__ == "__main__":
    for n, expected in tests:
        result = isPower2(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} isPower2({n}) = {result}")
