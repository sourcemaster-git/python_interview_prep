def countdigits(x: int) -> int:
    res = 0
    x = abs(x)
    while x > 0:
        x = x // 10
        res += 1
    return res


tests = [
    (1, 1),
    (12, 2),
    (123, 3),
    (1234, 4),
    (99999, 5),
    (0, 0),
    (10, 2),
    (100, 3),
    (1000000, 7),
    (9, 1),
    (99, 2),
]

for x, expected in tests:
    result = countdigits(x)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} countdigits({x}) = {result}")


"""
```

**Output:**
```
PASS countdigits(1) = 1
PASS countdigits(12) = 2
PASS countdigits(123) = 3
PASS countdigits(1234) = 4
PASS countdigits(99999) = 5
PASS countdigits(0) = 0
PASS countdigits(10) = 2
PASS countdigits(100) = 3
PASS countdigits(1000000) = 7
PASS countdigits(9) = 1
PASS countdigits(99) = 2
"""
