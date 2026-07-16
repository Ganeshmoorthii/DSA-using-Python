# Valid Palindrome

## Problem Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

**

## Examples

Example 1:**

```
**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.
```

**Example 3:**

```
**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**

## Constraints

Constraints:**

	- `1 <= s.length <= 2 * 10^5`

	- `s` consists only of printable ASCII characters.

---

## Submission — 16 Jul 2026, 11:24 am (PYTHON3)

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip().replace(" ","")
        l=0
        r=len(s)-1
        while l<r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1
        return True 

```
