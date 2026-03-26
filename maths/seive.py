# LOGIC:
# ============================================================================
# SIEVE OF ERATOSTHENES ALGORITHM
# ============================================================================
#
# Core Principle:
# --------------
# A prime number is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. The Sieve of Eratosthenes finds all primes up to n
# by iteratively marking multiples of each prime as composite.
#
# Algorithm Steps:
# --------------
# 1. Create a boolean array isPrime[0..n] initialized to True
#    - Index represents the number
#    - Value indicates if the number is potentially prime
#
# 2. Set base cases:
#    - isPrime[0] = False (0 is not prime)
#    - isPrime[1] = False (1 is not prime)
#
# 3. For each number i from 2 to sqrt(n):
#    - If isPrime[i] is True (i is prime):
#      - Mark all multiples of i as False (composite)
#      - Start marking from i*i (optimization)
#      - Reason: Any multiple k*i where k < i has already been marked by a smaller prime
#      - Increment by i to get next multiple
#
# 4. Collect all indices where isPrime[i] is True
#    - These are the prime numbers from 2 to n
#
# Optimizations Used:
# ------------------
# 1. Only sieve up to sqrt(n) - factors beyond sqrt(n) are paired with factors below
# 2. Start marking from i*i - avoids redundant marking
# 3. Use step of i for multiples - efficient iteration
#
# Time Complexity Analysis:
# ------------------------
# Let n be the input number
#
# The algorithm performs:
# - For each prime p ≤ √n, we mark n/p numbers
# - Total operations = Σ(n/p) for primes p ≤ √n
#
# By the Prime Number Theorem, the sum of reciprocals of primes up to x is ≈ log log x
# Therefore: Σ(n/p) ≈ n * log log √n ≈ n * log log n
#
# Final Time Complexity: O(n log log n)
#
# Space Complexity: O(n) - for the boolean array
#
# Example Walkthrough (n = 30):
# ----------------------------
# Initial: [T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T]
#          indices: 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
#
# Set base: isPrime[0]=F, isPrime[1]=F
# Step 1: i=2 (prime) -> mark 4,6,8,10,12,14,16,18,20,22,24,26,28,30 as composite
# Step 2: i=3 (prime) -> mark 9,15,21,27 as composite
# Step 3: i=5 (prime) -> mark 25 as composite
# Step 4: i=7 (7*7=49>30) -> stop
#
# Remaining True: indices 2,3,5,7,11,13,17,19,23,29
# Result: [2,3,5,7,11,13,17,19,23,29]
# ============================================================================

from typing import List


def sieve(n: int) -> List[int]:
    """
    Find all prime numbers up to n using Sieve of Eratosthenes.

    Args:
        n: Upper limit to find primes (inclusive)

    Returns:
        List of all prime numbers ≤ n

    Time Complexity: O(n log log n)
    Space Complexity: O(n)

    Example:
        sieve(10) -> [2, 3, 5, 7]
        sieve(20) -> [2, 3, 5, 7, 11, 13, 17, 19]
    """
    # Edge case: No primes less than 2
    if n < 2:
        return []

    # Step 1: Initialize boolean array
    # is_prime[i] = True means i is potentially prime
    # Initially assume all numbers are prime
    is_prime = [True] * (n + 1)

    # Step 2: Set base cases
    # 0 and 1 are not prime numbers
    is_prime[0] = False
    is_prime[1] = False

    # Step 3: Sieve process
    # Only need to check up to sqrt(n)
    # Because if n = a * b, at least one factor ≤ sqrt(n)
    i = 2
    while i * i <= n:
        # If i is still marked as prime, it's actually prime
        if is_prime[i]:
            # Mark all multiples of i as composite
            # Start from i*i because smaller multiples (i*2, i*3, ..., i*(i-1))
            # have already been marked by smaller primes
            j = i * i
            while j <= n:
                is_prime[j] = False  # Mark as composite
                j += i  # Move to next multiple
        i += 1  # Check next number

    # Step 4: Collect results
    # Iterate through array and collect indices where is_prime is True
    primes = []
    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


# ADDITIONAL OPTIMIZED VERSION WITH DETAILED COMPLEXITY ANALYSIS
# ============================================================================


def sieve_optimized(n: int) -> List[int]:
    """
    Optimized Sieve of Eratosthenes with early termination and list comprehension.

    Time Complexity: O(n log log n) - same theoretical complexity but with better constants
    Space Complexity: O(n)

    Optimizations:
    1. Use list comprehension for result collection
    2. Use for loops instead of while loops (often faster in Python)
    3. Pre-allocate array with appropriate size
    """
    if n < 2:
        return []

    # Initialize sieve array
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve: only need to go up to sqrt(n)
    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if is_prime[i]:
            # Mark multiples starting from i*i with step i
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Collect primes using list comprehension
    return [i for i in range(2, n + 1) if is_prime[i]]


# COMPLEXITY VISUALIZATION FUNCTION
# ============================================================================


def analyze_complexity():
    """
    Analyze and visualize the time complexity of the sieve algorithm.
    """
    import time
    import math

    print("=" * 70)
    print("SIEVE OF ERATOSTHENES - COMPLEXITY ANALYSIS")
    print("=" * 70)

    # Test different input sizes
    test_sizes = [1000, 10000, 50000, 100000, 500000, 1000000]

    print(
        f"\n{'n':<10} {'Primes Found':<15} {'Time (seconds)':<15} {'n log log n':<15}"
    )
    print("-" * 70)

    for n in test_sizes:
        # Measure execution time
        start_time = time.time()
        primes = sieve(n)
        elapsed_time = time.time() - start_time

        # Calculate theoretical complexity value
        if n > 1:
            log_log_n = math.log(math.log(n)) if n > 2 else 0
            complexity_value = n * log_log_n
        else:
            complexity_value = 0

        print(
            f"{n:<10} {len(primes):<15} {elapsed_time:<15.6f} {complexity_value:<15.2f}"
        )

    print("\n" + "=" * 70)
    print("COMPLEXITY EXPLANATION:")
    print("=" * 70)
    print("""
    Time Complexity: O(n log log n)
    ---------------------------------
    - n: Number of elements to check
    - log log n: Number of primes up to √n (approximately)
    - Each prime p marks approximately n/p numbers
    - Sum over primes: n * (1/2 + 1/3 + 1/5 + 1/7 + ...) ≈ n * log log n
    
    Why not O(n log n)?
    - The sum of reciprocals of primes diverges slower than harmonic series
    - 1/2 + 1/3 + 1/5 + 1/7 + ... = O(log log n)
    - Hence total operations = n * O(log log n) = O(n log log n)
    
    Space Complexity: O(n)
    ----------------------
    - We maintain a boolean array of size n+1
    - Each element stores a boolean (True/False)
    - Additional O(k) space for result, where k is number of primes
    - k ≈ n / log n (by Prime Number Theorem)
    - Total space: O(n) + O(n/log n) = O(n)
    """)

    return primes


# PERFORMANCE COMPARISON WITH BRUTE FORCE
# ============================================================================


def is_prime_bruteforce(n: int) -> bool:
    """
    Brute force primality test for comparison.
    Time Complexity: O(√n) per number
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def find_primes_bruteforce(n: int) -> List[int]:
    """
    Find primes using brute force for comparison.
    Time Complexity: O(n√n)
    """
    return [i for i in range(2, n + 1) if is_prime_bruteforce(i)]


def compare_performance():
    """
    Compare performance between Sieve and Brute Force.
    """
    import time

    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON: SIEVE vs BRUTE FORCE")
    print("=" * 70)

    test_sizes = [1000, 5000, 10000, 20000]

    print(f"\n{'n':<10} {'Sieve Time (s)':<18} {'Brute Force (s)':<18} {'Speedup':<10}")
    print("-" * 70)

    for n in test_sizes:
        # Time Sieve
        start = time.time()
        sieve_primes = sieve(n)
        sieve_time = time.time() - start

        # Time Brute Force
        start = time.time()
        brute_primes = find_primes_bruteforce(n)
        brute_time = time.time() - start

        # Calculate speedup
        speedup = brute_time / sieve_time if sieve_time > 0 else 0

        print(f"{n:<10} {sieve_time:<18.6f} {brute_time:<18.6f} {speedup:<10.2f}x")

        # Verify results match
        assert sieve_primes == brute_primes, "Results don't match!"

    print("\n" + "=" * 70)
    print("CONCLUSION: Sieve is significantly faster for large n due to O(n log log n)")
    print("           vs O(n√n) for brute force approach.")
    print("=" * 70)


# VISUAL REPRESENTATION OF SIEVE PROCESS
# ============================================================================


def visualize_sieve_process(n: int = 50):
    """
    Visualize how the sieve algorithm works step by step.
    """
    print("\n" + "=" * 70)
    print(f"VISUALIZATION: Sieve of Eratosthenes (n = {n})")
    print("=" * 70)

    # Initialize
    numbers = list(range(n + 1))
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    def display_state(current_prime=None):
        """Display current state of numbers"""
        line = ""
        for num in range(2, n + 1):
            if num == current_prime:
                line += f"\033[92m[{num:3}]\033[0m"  # Green for current prime
            elif not is_prime[num]:
                line += f"\033[91m{num:5}\033[0m"  # Red for composite
            else:
                line += f"{num:5}"  # Normal for prime candidates
            if num % 10 == 0 and num != n:
                line += "\n"
        print(line)

    print("\nInitial state (all numbers considered prime):")
    display_state()

    # Sieve process
    i = 2
    step = 1
    while i * i <= n:
        if is_prime[i]:
            print(f"\nStep {step}: Found prime {i}")
            print(f"Marking multiples of {i}: ", end="")
            marked = []
            for j in range(i * i, n + 1, i):
                if is_prime[j]:
                    is_prime[j] = False
                    marked.append(j)
            print(marked)
            print(f"State after marking multiples of {i}:")
            display_state(i)
            step += 1
        i += 1

    # Final result
    primes = [num for num in range(2, n + 1) if is_prime[num]]
    print(f"\n{'='*70}")
    print(f"FINAL RESULT: {len(primes)} primes found up to {n}")
    print(f"Primes: {primes}")
    print(f"{'='*70}")


# RUN ALL ANALYSES
# ============================================================================

if __name__ == "__main__":
    # Run complexity analysis
    analyze_complexity()

    # Compare performance
    compare_performance()

    # Visualize the sieve process
    visualize_sieve_process(50)

    # Quick test
    print("\n" + "=" * 70)
    print("QUICK TEST")
    print("=" * 70)
    print(f"sieve(10): {sieve(10)}")
    print(f"sieve(20): {sieve(20)}")
    print(f"sieve(30): {sieve(30)}")
    print(f"sieve(100): {sieve(100)[:10]}... (total: {len(sieve(100))} primes)")
