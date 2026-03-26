# LOGIC:
# This function finds all prime factors of a given number n.
#
# 1. Handle edge cases:
#    - If n <= 1, return empty list (no prime factors)
#
# 2. Initialize:
#    - ans: list to store prime factors
#    - temp: working variable for division
#
# 3. Handle factor 2:
#    - Check if n is divisible by 2
#    - Repeatedly divide by 2 and append 2 to ans while divisible
#
# 4. Handle factor 3:
#    - Check if n is divisible by 3
#    - Repeatedly divide by 3 and append 3 to ans while divisible
#
# 5. Handle remaining prime factors (5 and above):
#    - Only need to check numbers of form 6k ± 1
#    - For each i (starting at 5), check i and i+2
#    - For each divisor found, repeatedly divide and append to ans
#    - Continue up to √n
#
# 6. Return list of all prime factors
#
# Time Complexity: O(√n)
# Space Complexity: O(log n) for storing factors

from typing import List


def print_prime(n: int) -> List[int]:
    """
    Return all prime factors of a number n.

    Args:
        n: Integer to factorize

    Returns:
        List of prime factors (with repetitions)

    Example:
        print_prime(12) -> [2, 2, 3]
        print_prime(13) -> [13]
        print_prime(1) -> []
    """

    # Edge case: numbers <= 1 have no prime factors
    if n <= 1:
        return []

    ans = []
    temp = n

    # Handle factor 2 (the only even prime)
    # Keep dividing by 2 while divisible
    while temp % 2 == 0:
        ans.append(2)
        temp //= 2

    # Handle factor 3
    while temp % 3 == 0:
        ans.append(3)
        temp //= 3

    # Handle remaining prime factors using 6k ± 1 optimization
    i = 5
    while i * i <= temp:  # Only need to check up to √temp
        # Check divisor i (6k-1)
        while temp % i == 0:
            ans.append(i)
            temp //= i

        # Check divisor i+2 (6k+1)
        while temp % (i + 2) == 0:
            ans.append(i + 2)
            temp //= i + 2

        i += 6  # Move to next pair

    # If temp > 1, it's a prime factor larger than √original n
    if temp > 1:
        ans.append(temp)

    return ans


def test_prime_factors():
    """Test cases for prime factorization"""

    test_cases = [
        (1, []),  # No factors
        (2, [2]),  # Prime number
        (3, [3]),  # Prime number
        (4, [2, 2]),  # Power of 2
        (6, [2, 3]),  # Product of 2 primes
        (8, [2, 2, 2]),  # 2³
        (9, [3, 3]),  # 3²
        (12, [2, 2, 3]),  # 2² × 3
        (13, [13]),  # Prime
        (16, [2, 2, 2, 2]),  # 2⁴
        (18, [2, 3, 3]),  # 2 × 3²
        (20, [2, 2, 5]),  # 2² × 5
        (24, [2, 2, 2, 3]),  # 2³ × 3
        (25, [5, 5]),  # 5²
        (27, [3, 3, 3]),  # 3³
        (30, [2, 3, 5]),  # 2 × 3 × 5
        (36, [2, 2, 3, 3]),  # 2² × 3²
        (49, [7, 7]),  # 7²
        (64, [2, 2, 2, 2, 2, 2]),  # 2⁶
        (84, [2, 2, 3, 7]),  # 2² × 3 × 7
        (97, [97]),  # Large prime
        (100, [2, 2, 5, 5]),  # 10²
        (121, [11, 11]),  # 11²
        (169, [13, 13]),  # 13²
        (999, [3, 3, 3, 37]),  # 3³ × 37
        (1000, [2, 2, 2, 5, 5, 5]),  # 10³
    ]

    print("Testing prime factorization:")
    print("-" * 40)

    for num, expected in test_cases:
        result = print_prime(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} {num:4} -> {result} (expected: {expected})")

    # Test large number
    print("\nTesting large number:")
    large_num = 2 * 2 * 3 * 5 * 7 * 11 * 13  # 60060
    result = print_prime(large_num)
    print(f"{large_num} -> {result}")
    print(f"Product of factors: {eval('*'.join(map(str, result)))}")


# Run tests
test_prime_factors()
