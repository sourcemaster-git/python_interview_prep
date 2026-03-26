def isPal(n: int) -> int:
    if n < 0:
        return False
    rev = 0
    temp = n
    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    return rev == n


tests = [
    (121, True),
    (1221, True),
    (12321, True),
    (123, False),
    (0, True),
    (1, True),
    (11, True),
    (12, False),
    (1001, True),
    (10, False),
    (-121, False),
]

for n, expected in tests:
    result = isPal(n)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} isPal({n}) = {result}")
