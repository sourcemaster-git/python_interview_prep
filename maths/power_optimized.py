# ============================================================================
# POWER FUNCTION IMPLEMENTATIONS
# ============================================================================
#
# LOGIC FOR POWER_RECURSIVE (Exponentiation by Squaring):
# -----------------------------------------------------
# This algorithm uses the mathematical property:
#   x^n = (x^(n/2))^2 if n is even
#   x^n = (x^(n/2))^2 * x if n is odd
#
# Algorithm Steps:
# 1. Base case: if n == 0, return 1 (any number to power 0 is 1)
# 2. Recursively compute temp = x^(n//2) (floor division)
# 3. If n is even: return temp * temp
# 4. If n is odd: return temp * temp * x
#
# Time Complexity: O(log n) - each recursive call reduces n by half
# Space Complexity: O(log n) - due to recursion stack depth
#
# LOGIC FOR POWER_ITERATIVE (Binary Exponentiation):
# ------------------------------------------------
# This algorithm uses the binary representation of exponent n:
#   x^n = x^(b_k b_{k-1} ... b_0)_2 = product of x^(2^i) for bits set to 1
#
# Algorithm Steps:
# 1. Initialize result = 1
# 2. While n > 0:
#    - If current bit of n is 1 (n % 2 == 1): multiply result by current x
#    - Square x for next bit position (x = x * x)
#    - Remove the processed bit (n //= 2)
# 3. Return result
#
# Time Complexity: O(log n) - processes each bit of exponent
# Space Complexity: O(1) - uses only constant extra space
#
# Example: x^13 = x^(1101)_2 = x^8 * x^4 * x^1
# ============================================================================


def power_recursive(x: int, n: int) -> int:
    """
    Compute x raised to power n using recursive exponentiation by squaring.

    Args:
        x: Base number
        n: Exponent (non-negative integer)

    Returns:
        x^n as integer

    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack

    Example:
        power_recursive(2, 10) -> 1024
        power_recursive(3, 4) -> 81
    """
    # Base case: any number to the power 0 is 1
    if n == 0:
        return 1

    # Recursively compute x^(n//2)
    temp = power_recursive(x, n // 2)

    # If exponent is even: x^n = (x^(n/2))^2
    # If exponent is odd: x^n = (x^(n/2))^2 * x
    if n % 2 == 0:
        return temp * temp  
    else:
        return temp * temp * x


def power_iterative(x: int, n: int) -> int:
    """
    Compute x raised to power n using iterative binary exponentiation.

    Args:
        x: Base number
        n: Exponent (non-negative integer)

    Returns:
        x^n as integer

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Example:
        power_iterative(2, 10) -> 1024
        power_iterative(3, 4) -> 81
    """
    result = 1

    # Process each bit of the exponent
    while n > 0:
        # If current bit is 1, multiply result by current x
        if n % 2 != 0:
            result *= x

        # Square x for the next bit position (x^(2^k))
        x *= x

        # Remove the processed bit (shift right)
        n //= 2

    return result


# CORRECTED RECURSIVE VERSION
# ============================================================================


def power_recursive_corrected(x: int, n: int) -> int:
    """
    Corrected recursive power function with proper handling of even/odd cases.

    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    if n == 0:
        return 1

    temp = power_recursive_corrected(x, n // 2)

    # Key fix: both cases need to square temp
    if n % 2 == 0:
        return temp * temp  # Fixed: was returning temp incorrectly
    else:
        return temp * temp * x


# ALTERNATIVE IMPLEMENTATIONS
# ============================================================================


def power_recursive_alt(x: int, n: int) -> int:
    """
    Alternative recursive implementation with clearer structure.
    """
    if n == 0:
        return 1

    if n % 2 == 0:
        # Even case: x^n = (x^(n/2))^2
        half = power_recursive_alt(x, n // 2)
        return half * half
    else:
        # Odd case: x^n = x * (x^((n-1)/2))^2
        half = power_recursive_alt(x, (n - 1) // 2)
        return x * half * half


def power_tail_recursive(x: int, n: int, acc: int = 1) -> int:
    """
    Tail recursive version (optimized for languages with TCO).

    Args:
        x: Base
        n: Exponent
        acc: Accumulator (result so far)

    Time Complexity: O(log n)
    Space Complexity: O(log n) (but can be optimized to O(1) with TCO)
    """
    if n == 0:
        return acc

    if n % 2 == 0:
        # Even: square base, halve exponent
        return power_tail_recursive(x * x, n // 2, acc)
    else:
        # Odd: multiply accumulator by base, reduce exponent
        return power_tail_recursive(x * x, n // 2, acc * x)


# TEST CASES AND VALIDATION
# ============================================================================


def test_power_functions():
    """Comprehensive test cases for power functions."""

    test_cases = [
        # (x, n, expected)
        (2, 0, 1),  # Any number to power 0
        (2, 1, 2),  # Power 1
        (2, 2, 4),  # Even exponent
        (2, 3, 8),  # Odd exponent
        (2, 5, 32),  # Small odd
        (2, 10, 1024),  # Medium
        (3, 0, 1),
        (3, 1, 3),
        (3, 2, 9),
        (3, 3, 27),
        (3, 4, 81),
        (5, 3, 125),
        (10, 3, 1000),
        (2, 15, 32768),  # Larger exponent
        (1, 100, 1),  # Base 1
        (-2, 3, -8),  # Negative base, odd exponent
        (-2, 4, 16),  # Negative base, even exponent
        (0, 5, 0),  # Base 0
        (0, 0, 1),  # 0^0 is conventionally 1
    ]

    print("=" * 70)
    print("TESTING POWER FUNCTIONS")
    print("=" * 70)

    for x, n, expected in test_cases:
        # Test corrected recursive version
        result_rec = power_recursive_corrected(x, n)
        status_rec = "✓" if result_rec == expected else "✗"

        # Test iterative version
        result_iter = power_iterative(x, n)
        status_iter = "✓" if result_iter == expected else "✗"

        # Test alternative recursive version
        result_alt = power_recursive_alt(x, n)
        status_alt = "✓" if result_alt == expected else "✗"

        # Test tail recursive version
        result_tail = power_tail_recursive(x, n)
        status_tail = "✓" if result_tail == expected else "✗"

        print(f"\n{x}^{n} = {expected}")
        print(f"  Recursive: {result_rec:10} {status_rec}")
        print(f"  Iterative: {result_iter:10} {status_iter}")
        print(f"  Alternate: {result_alt:10} {status_alt}")
        print(f"  Tail Rec:  {result_tail:10} {status_tail}")

        # Verify all match
        assert all(
            v == expected for v in [result_rec, result_iter, result_alt, result_tail]
        )


# VISUALIZATION OF BINARY EXPONENTIATION
# ============================================================================


def visualize_binary_exponentiation(x: int, n: int):
    """
    Visualize how binary exponentiation works step by step.
    """
    print("\n" + "=" * 70)
    print(f"VISUALIZATION: {x}^{n} using Binary Exponentiation")
    print("=" * 70)

    print(f"\nBinary representation of exponent {n}: {bin(n)[2:]}")
    print("\nStep-by-step calculation:")
    print("-" * 50)

    result = 1
    base = x
    exp = n
    step = 1

    while exp > 0:
        bit = exp % 2
        print(f"\nStep {step}:")
        print(f"  Current bit: {bit} ({'set' if bit else 'clear'})")
        print(f"  Current base value: {base}^{2**(step-1)} = {base}")

        if bit:
            result *= base
            print(f"  Bit is set, multiply result by {base} → result = {result}")
        else:
            print(f"  Bit is clear, no multiplication")

        print(f"  Square base for next bit: {base} × {base} = {base * base}")
        base *= base
        exp //= 2
        step += 1

    print(f"\n{'='*50}")
    print(f"FINAL RESULT: {x}^{n} = {result}")
    print(f"{'='*50}")


# COMPLEXITY ANALYSIS VISUALIZATION
# ============================================================================


def analyze_power_complexity():
    """
    Analyze and visualize the time complexity of power functions.
    """
    import time
    import math

    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS: Power Functions")
    print("=" * 70)

    x = 2  # Fixed base for testing

    # Test different exponent sizes
    exponents = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

    print(
        f"\n{'n (exponent)':<15} {'Recursive (s)':<15} {'Iterative (s)':<15} {'log2(n)':<10}"
    )
    print("-" * 70)

    for n in exponents:
        # Test recursive version
        start = time.time()
        result_rec = power_recursive_corrected(x, n)
        rec_time = time.time() - start

        # Test iterative version
        start = time.time()
        result_iter = power_iterative(x, n)
        iter_time = time.time() - start

        log2_n = math.log2(n)

        print(f"{n:<15} {rec_time:<15.6f} {iter_time:<15.6f} {log2_n:<10.2f}")

        # Verify results match
        assert result_rec == result_iter

    print("\n" + "=" * 70)
    print("COMPLEXITY EXPLANATION:")
    print("=" * 70)
    print("""
    Time Complexity: O(log n)
    -------------------------
    - Both algorithms process the binary digits of the exponent
    - Number of iterations = number of bits in exponent ≈ log2(n)
    - Each iteration does O(1) operations
    - Total: O(log n) operations
    
    Space Complexity:
    -----------------
    - Iterative: O(1) - only uses a few variables
    - Recursive: O(log n) - due to recursion stack depth
    - Tail recursive: O(log n) but can be optimized to O(1) with TCO
    
    Why O(log n) is better than O(n):
    ---------------------------------
    - Naive approach would multiply x n times: O(n)
    - Binary exponentiation reduces to O(log n)
    - For n = 1,000,000: O(n) would take 1,000,000 operations
                       O(log n) takes only ~20 operations!
    """)


# DEMONSTRATION OF BUG IN ORIGINAL RECURSIVE FUNCTION
# ============================================================================


def demonstrate_bug():
    """
    Demonstrate the bug in the original recursive implementation.
    """
    print("\n" + "=" * 70)
    print("BUG DEMONSTRATION: Original Recursive Implementation")
    print("=" * 70)

    # Original buggy function
    def power_recursive_buggy(x: int, n: int) -> int:
        if n == 0:
            return 1
        temp = power_recursive_buggy(x, n // 2)
        if n % 2 == 0:
            return temp  # BUG: Should be temp * temp
        else:
            return temp * x  # BUG: Should be temp * temp * x

    print("\nTesting buggy implementation:")
    test_values = [(2, 2), (2, 4), (3, 2), (3, 4)]

    for x, n in test_values:
        buggy = power_recursive_buggy(x, n)
        correct = power_recursive_corrected(x, n)
        print(f"{x}^{n}: Buggy = {buggy}, Correct = {correct}")

        if buggy != correct:
            print(f"  ✗ BUG: Expected {correct}, got {buggy}")
            print(f"  Reason: Missing multiplication by temp in both cases")

    print("\n" + "=" * 70)
    print("FIX: Both even and odd cases should multiply temp * temp")
    print("     Even: temp * temp")
    print("     Odd:  temp * temp * x")
    print("=" * 70)


# PERFORMANCE COMPARISON WITH NAIVE APPROACH
# ============================================================================


def power_naive(x: int, n: int) -> int:
    """
    Naive implementation for comparison.
    Time Complexity: O(n)
    """
    result = 1
    for _ in range(n):
        result *= x
    return result


def compare_with_naive():
    """
    Compare binary exponentiation with naive approach.
    """
    import time

    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON: Binary Exponentiation vs Naive")
    print("=" * 70)

    x = 2
    exponents = [1000, 10000, 50000, 100000, 500000, 1000000]

    print(f"\n{'n':<12} {'Binary (s)':<15} {'Naive (s)':<15} {'Speedup':<10}")
    print("-" * 70)

    for n in exponents:
        # Test binary exponentiation
        start = time.time()
        binary_result = power_iterative(x, n)
        binary_time = time.time() - start

        # Test naive approach
        start = time.time()
        naive_result = power_naive(x, n)
        naive_time = time.time() - start

        speedup = naive_time / binary_time if binary_time > 0 else 0

        print(f"{n:<12} {binary_time:<15.6f} {naive_time:<15.6f} {speedup:<10.2f}x")

        # Verify results match
        assert binary_result == naive_result

    print("\n" + "=" * 70)
    print("CONCLUSION: Binary exponentiation is exponentially faster for large n")
    print(
        f"            Speedup factor increases with n, reaching > {speedup:.0f}x for n={exponents[-1]}"
    )
    print("=" * 70)


# RUN ALL ANALYSES
# ============================================================================

if __name__ == "__main__":
    # Test all implementations
    test_power_functions()

    # Demonstrate the bug
    demonstrate_bug()

    # Visualize binary exponentiation
    visualize_binary_exponentiation(3, 13)

    # Analyze complexity
    analyze_power_complexity()

    # Compare with naive approach
    compare_with_naive()

    # Quick examples
    print("\n" + "=" * 70)
    print("QUICK EXAMPLES")
    print("=" * 70)
    print(f"2^10 = {power_iterative(2, 10)}")
    print(f"3^8 = {power_iterative(3, 8)}")
    print(f"5^5 = {power_iterative(5, 5)}")
    print(f"(-2)^3 = {power_iterative(-2, 3)}")
    print(f"2^20 = {power_iterative(2, 20)}")
