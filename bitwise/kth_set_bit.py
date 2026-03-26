# ------------------------------------------------------------
# K-th Set Bit Checker
# ------------------------------------------------------------
# Logic:
# To check whether the k-th bit (1-based index) in integer n is set:
#
# 1. Create a mask by shifting 1 left by (k - 1)
#       mask = 1 << (k - 1)
#
# 2. Perform bitwise AND with n:
#       n & mask
#
# 3. If result != 0 → bit is SET
#    else → bit is NOT SET
#
# Example:
# n = 5  -> binary: 101
# k = 3
# mask = 1 << 2 = 100
# 101 & 100 = 100 → Yes (bit is set)
# ------------------------------------------------------------


def kth_set_bit(n: int, k: int) -> str:
    if (n & (1 << (k - 1))) != 0:
        return "Yes"
    else:
        return "No"


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
tests = [
    (5, 1, "Yes"),  # 101 → bit 1
    (5, 2, "No"),
    (5, 3, "Yes"),
    (8, 4, "Yes"),  # 1000
    (8, 3, "No"),
    (1, 1, "Yes"),
    (0, 1, "No"),
    (10, 2, "Yes"),  # 1010
    (10, 3, "No"),
]


# ------------------------------------------------------------
# Run Tests
# ------------------------------------------------------------
if __name__ == "__main__":
    for n, k, expected in tests:
        result = kth_set_bit(n, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} kth_set_bit({n}, {k}) = {result}")
