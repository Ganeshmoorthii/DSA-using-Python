# Reverse Integer

## Problem Description

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**

## Examples

Example 1:**

```
**Input:** x = 123
**Output:** 321
```

**Example 2:**

```
**Input:** x = -123
**Output:** -321
```

**Example 3:**

```
**Input:** x = 120
**Output:** 21
```

**

## Constraints

Constraints:**

	- `-2^31 <= x <= 2^31 - 1`

---

## Submission — 16 Jul 2026, 11:59 am (PYTHON3)

```py
123
-123
120
```

---

## Submission — 17 Jul 2026, 11:20 am (PYTHON3)

```py
123
-123
120
```

---

## Submission — 17 Jul 2026, 11:27 am (PYTHON3)

```py
class Solution:
    def reverse(self, x: int) -> int:
        isNeg=x<0
        x = -x if isNeg else x
        res = int(str(x)[::-1])
        if res < -2**31 or res > 2**31-1:
            return 0
        return -res if isNeg else res

```
