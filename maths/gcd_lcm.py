def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


tests_gcd = [
    ((12, 8), 4),
    ((18, 12), 6),
    ((7, 5), 1),
    ((0, 5), 5),
    ((5, 0), 5),
    ((0, 0), 0),
    ((7, 7), 7),
    ((1, 99), 1),
]

tests_lcm = [
    ((4, 6), 12),
    ((3, 5), 15),
    ((12, 18), 36),
    ((7, 14), 14),
    ((1, 5), 5),
    ((5, 5), 5),
]

for (a, b), expected in tests_gcd:
    result = gcd(a, b)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} gcd({a}, {b}) = {result}")

print()

for (a, b), expected in tests_lcm:
    result = lcm(a, b)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} lcm({a}, {b}) = {result}")
