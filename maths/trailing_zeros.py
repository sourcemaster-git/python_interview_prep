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
