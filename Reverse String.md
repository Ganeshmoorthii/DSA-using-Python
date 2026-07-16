# Reverse String

## Problem Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

**

## Examples

Example 1:**

```
**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]
```
**Example 2:**

```
**Input:** s = ["H","a","n","n","a","h"]
**Output:** ["h","a","n","n","a","H"]
```

**

## Constraints

Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is a printable ascii character.

---

## Submission — 16 Jul 2026, 11:14 am (PYTHON3)

```py
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l<=r:
            temp = s[r]
            s[r]=s[l]
            s[l]=temp
            l+=1
            r-=1

```

---

## Submission — 16 Jul 2026, 11:16 am (PYTHON3)

```py
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l<=r:
            temp = s[r]
            s[r]=s[l]
            s[l]=temp
            l+=1
            r-=1

```
