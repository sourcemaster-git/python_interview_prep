# ------------------------------------------------------------
# Problem: Find Two Numbers Occurring Odd Number of Times
# ------------------------------------------------------------
# Given an array where:
# - Exactly TWO elements occur an odd number of times
# - All other elements occur an even number of times
#
# Goal:
# Return the two odd-occurring elements
#
# ------------------------------------------------------------
# Core Idea: XOR + Bit Manipulation
# ------------------------------------------------------------
# XOR Properties:
# 1. x ^ x = 0        (same numbers cancel out)
# 2. x ^ 0 = x
# 3. XOR is commutative and associative
#
# ------------------------------------------------------------
# Step-by-Step Logic
# ------------------------------------------------------------
#
# STEP 1: XOR all elements
#
# Let the two odd occurring numbers be: a and b
#
# After XOR-ing entire array:
#   xor = a ^ b
#
# Why?
# - All even-occurring numbers cancel out
# - Only a and b remain
#
# ------------------------------------------------------------
# STEP 2: Find a differentiating bit
#
# We need to separate 'a' and 'b'.
# Since a != b → their XOR has at least one set bit.
#
# We extract the RIGHTMOST SET BIT:
#
#   sb = xor & -xor
#
# Why this works:
# - -xor is 2’s complement of xor
# - xor & -xor isolates the lowest set bit
#
# Example:
#   xor = 6 (110)
#   -xor = -6 → (two's complement) = 010
#   sb = 110 & 010 = 010
#
# This bit is different in a and b
#
# ------------------------------------------------------------
# STEP 3: Divide into two groups
#
# Using sb, partition elements:
#
# Group A → elements where (bit is set)
# Group B → elements where (bit is NOT set)
#
# Why this works:
# - a and b fall into DIFFERENT groups
# - all other numbers still cancel within their group
#
# ------------------------------------------------------------
# STEP 4: XOR each group
#
# Group A XOR → gives one odd number
# Group B XOR → gives the other
#
# ------------------------------------------------------------
# Final Result: (a, b)
# ------------------------------------------------------------


from typing import List, Tuple


def two_odd_occuring(arr: List[int]) -> Tuple[int, int]:
    a, b = 0, 0

    # STEP 1: XOR all elements → a ^ b
    xor = 0
    for item in arr:
        xor ^= item

    # STEP 2: isolate rightmost set bit
    sb = xor & -xor

    # STEP 3: divide into two groups and XOR separately
    for item in arr:
        if (item & sb) != 0:
            a ^= item
        else:
            b ^= item

    return (a, b)


# ------------------------------------------------------------
# Dry Run Example
# ------------------------------------------------------------
# arr = [1, 2, 3, 2, 3, 1, 3, 4]
#
# Step 1:
# XOR all → 3 ^ 4 = 7 (111)
#
# Step 2:
# sb = 7 & -7 = 001
#
# Step 3:
# Group 1 (bit set): 1, 3, 1, 3 → XOR = 3
# Group 2 (bit not set): 2, 2, 4 → XOR = 4
#
# Result: (3, 4)
# ------------------------------------------------------------


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
tests = [
    ([1, 2, 3, 2, 3, 1, 3, 4], (3, 4)),
    ([4, 4, 5, 5, 6, 7], (6, 7)),
    ([10, 20, 10, 30, 20, 40], (30, 40)),
    ([7, 3, 5, 3, 5, 7, 9, 11], (9, 11)),
]


# ------------------------------------------------------------
# Run Tests
# ------------------------------------------------------------
if __name__ == "__main__":
    for arr, expected in tests:
        result = two_odd_occuring(arr)

        # Order doesn't matter → compare as sets
        status = "PASS" if set(result) == set(expected) else "FAIL"

        print(f"{status} two_odd_occuring({arr}) = {result}")


# ------------------------------------------------------------
# Complexity Analysis
# ------------------------------------------------------------
# Time Complexity: O(n)
#   - One pass for XOR
#   - One pass for partitioning
#
# Space Complexity: O(1)
#   - No extra space used
#
# ------------------------------------------------------------
# Key Takeaways (Interview Ready)
# ------------------------------------------------------------
# 1. XOR cancels even occurrences
# 2. xor = a ^ b helps reduce problem
# 3. Rightmost set bit splits numbers cleanly
# 4. Partition + XOR gives final result
#
# ------------------------------------------------------------
