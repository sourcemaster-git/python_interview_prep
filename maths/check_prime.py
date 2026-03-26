# LOGIC:
# 1. Handle base cases:
#    - Numbers <= 1 are not prime
#    - 2 and 3 are prime numbers
#
# 2. Quick elimination:
#    - If n is divisible by 2 or 3, it's not prime
#
# 3. Optimized divisibility checking:
#    - All prime numbers > 3 can be expressed as 6k ± 1
#    - Start checking from i = 5 (which is 6×1 - 1)
#    - Only check numbers of the form 6k ± 1 up to √n
#    - Check i and i+2 (which are 6k-1 and 6k+1 respectively)
#    - Increment i by 6 to move to the next pair
#
# 4. If no divisors found, the number is prime
#
# Time Complexity: O(√n)
# Space Complexity: O(1)


def isPrime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: Integer to check for primality

    Returns:
        bool: True if prime, False otherwise
    """
    # Handle base cases for numbers <= 1
    if n <= 1:
        return False

    # 2 and 3 are prime
    if n <= 3:
        return True

    # Eliminate numbers divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisibility by numbers of form 6k ± 1
    i = 5  # Start with 5 (6×1 - 1)
    while i * i <= n:  # Only need to check up to square root
        # Check 6k-1 (i) and 6k+1 (i+2)
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Found a divisor
        i += 6  # Move to next pair: 5,7 → 11,13 → 17,19 → ...

    return True  # No divisors found, n is prime


def test_isPrime():
    """Test cases for isPrime function"""

    # Test small numbers
    print("Testing small numbers:")
    print(f"isPrime(1): {isPrime(1)}")  # False (not prime)
    print(f"isPrime(2): {isPrime(2)}")  # True (prime)
    print(f"isPrime(3): {isPrime(3)}")  # True (prime)
    print(f"isPrime(4): {isPrime(4)}")  # False (2×2)
    print(f"isPrime(5): {isPrime(5)}")  # True (prime)
    print(f"isPrime(6): {isPrime(6)}")  # False (2×3)

    # Test some prime numbers
    print("\nTesting prime numbers:")
    primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for p in primes:
        print(f"isPrime({p}): {isPrime(p)}")

    # Test some composite numbers
    print("\nTesting composite numbers:")
    composites = [9, 15, 21, 25, 27, 33, 35, 39, 45, 49]
    for c in composites:
        print(f"isPrime({c}): {isPrime(c)}")

    # Test edge cases
    print("\nTesting edge cases:")
    print(f"isPrime(0): {isPrime(0)}")  # False
    print(f"isPrime(-5): {isPrime(-5)}")  # False
    print(f"isPrime(100): {isPrime(100)}")  # False (10×10)
    print(f"isPrime(97): {isPrime(97)}")  # True (prime)
    print(f"isPrime(101): {isPrime(101)}")  # True (prime)

    # Test large numbers
    print("\nTesting large numbers:")
    print(f"isPrime(999983): {isPrime(999983)}")  # True (prime)
    print(f"isPrime(999984): {isPrime(999984)}")  # False
    print(f"isPrime(1000003): {isPrime(1000003)}")  # True (prime)


# Run tests
test_isPrime()
