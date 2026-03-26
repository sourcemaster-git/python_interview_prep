# Logic:
# Trailing zeros in n! (factorial) are created by factors of 10.
# Each 10 = 2 × 5. Since factorials have more 2s than 5s,
# the count of 5s determines the number of trailing zeros.
#
# So, we count how many multiples of 5 are present in n:
#   n // 5  → numbers contributing at least one 5
#   n // 25 → numbers contributing an extra 5 (like 25, 50, 75...)
#   n // 125 → extra contributions from higher powers of 5
#   ...
#
# Total trailing zeros = n//5 + n//25 + n//125 + ...

def trailing_zeros(n: int) -> int:
    res = 0
    i = 5
    while i <= n:
        res += n // i
        i *= 5
    return res


tests = [
    (0, 0),
    (1, 0),
    (4, 0),
    (5, 1),
    (10, 2),
    (15, 3),
    (20, 4),
    (25, 6),
    (50, 12),
    (100, 24),
    (125, 31),
]

for n, expected in tests:
    result = trailing_zeros(n)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} trailing_zeros({n}) = {result}")
