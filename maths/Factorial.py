def fact(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


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
