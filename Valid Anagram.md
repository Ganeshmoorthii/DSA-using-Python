# Valid Anagram

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**

## Examples

Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

**

## Constraints

Constraints:**

	- `1 <= s.length, t.length <= 5 * 10^4`

	- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## Submission — 15 Jul 2026, 11:22 am (PYTHON3)

### Valid Anagram

**Description:**

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**

**Examples:**

Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

**

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ind_s = ord(s[i]) - ord('a')
            ind_t = ord(t[i]) - ord('a')
            lookup[ind_s]+=1
            lookup[ind_t]-=1
        for i in s:
            ind_s = ord(i) - ord('a')
            if lookup[ind_s] != 0:
                return False
        return True
```

---

## Submission — 15 Jul 2026, 11:22 am (PYTHON3)

### Valid Anagram

**Description:**

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**

**Examples:**

Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

**

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ind_s = ord(s[i]) - ord('a')
            ind_t = ord(t[i]) - ord('a')
            lookup[ind_s]+=1
            lookup[ind_t]-=1
        for i in s:
            ind_s = ord(i) - ord('a')
            if lookup[ind_s] != 0:
                return False
        return True
```
