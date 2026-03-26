def fact(n: int) -> int:
    if n == 0:
        return 1

    return n * fact(n - 1)


tests = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (10, 3628800),
]

for n, expected in tests:
    result = fact(n)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} fact({n}) = {result}")
