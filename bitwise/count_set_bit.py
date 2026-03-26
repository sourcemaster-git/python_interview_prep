# ------------------------------------------------------------
# Count Set Bits (Brian Kernighan’s Algorithm)
# ------------------------------------------------------------
# Logic:
# Each iteration removes the lowest set bit from n:
#
#   n & (n - 1)
#
# Example:
# n = 10 (1010)
# Step 1: 1010 & 1001 = 1000
# Step 2: 1000 & 0111 = 0000
#
# Number of iterations = number of set bits
#
# This is more efficient than checking every bit.
# ------------------------------------------------------------


def count_set_bit(n: int) -> int:
    res = 0
    while n > 0:
        n &= n - 1
        res += 1
    return res


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
tests = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 1),
    (5, 2),  # 101
    (7, 3),  # 111
    (10, 2),  # 1010
    (15, 4),  # 1111
    (16, 1),
]


# ------------------------------------------------------------
# Run Tests
# ------------------------------------------------------------
if __name__ == "__main__":
    for n, expected in tests:
        result = count_set_bit(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} count_set_bit({n}) = {result}")
