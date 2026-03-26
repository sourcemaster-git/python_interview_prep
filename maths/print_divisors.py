from typing import List


def print_divisors(n: int) -> List[int]:
    """
    Return all divisors of a number n.

    Args:
        n: Integer to find divisors for (positive integer)

    Returns:
        List of all divisors in sorted order

    Example:
        print_divisors(12) -> [1, 2, 3, 4, 6, 12]
        print_divisors(16) -> [1, 2, 4, 8, 16]
        print_divisors(13) -> [1, 13]
    """
    # Handle edge cases
    if n <= 0:
        return []

    i = 1
    ans = []

    # Find all divisor pairs up to square root
    while i * i <= n:
        if n % i == 0:
            ans.append(i)  # Add the smaller divisor
            if i != n // i:  # Avoid duplicate for perfect squares
                ans.append(n // i)  # Add the larger divisor
        i += 1

    # Sort divisors for consistent output
    ans.sort()
    return ans


def test_print_divisors():
    """Test cases for divisor finding"""

    test_cases = [
        (1, [1]),  # Only divisor is 1
        (2, [1, 2]),  # Prime number
        (3, [1, 3]),  # Prime number
        (4, [1, 2, 4]),  # Perfect square
        (5, [1, 5]),  # Prime number
        (6, [1, 2, 3, 6]),  # Composite
        (7, [1, 7]),  # Prime number
        (8, [1, 2, 4, 8]),  # Power of 2
        (9, [1, 3, 9]),  # Perfect square
        (10, [1, 2, 5, 10]),  # Composite
        (12, [1, 2, 3, 4, 6, 12]),  # Multiple divisors
        (16, [1, 2, 4, 8, 16]),  # Perfect square
        (17, [1, 17]),  # Prime
        (18, [1, 2, 3, 6, 9, 18]),  # Composite
        (20, [1, 2, 4, 5, 10, 20]),  # Composite
        (25, [1, 5, 25]),  # Perfect square
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),  # Many divisors
        (49, [1, 7, 49]),  # Perfect square
        (64, [1, 2, 4, 8, 16, 32, 64]),  # Power of 2
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]),  # Composite
        (0, []),  # Edge case: zero
        (-12, []),  # Edge case: negative
    ]

    print("Testing print_divisors function:")
    print("-" * 50)

    for num, expected in test_cases:
        result = print_divisors(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} {num:4} -> {result} (expected: {expected})")

    # Additional test for perfect squares
    print("\nTesting perfect squares (no duplicates):")
    perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
    for num in perfect_squares:
        result = print_divisors(num)
        # Check for duplicates
        has_duplicates = len(result) != len(set(result))
        print(f"{num:4}: {result} {'✓' if not has_duplicates else '✗ Has duplicates!'}")


# Run tests
test_print_divisors()
