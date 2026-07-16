# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

**

## Examples

Example 1:**

```
**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.
```

**Example 2:**

```
**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.
```

**Example 3:**

```
**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**

## Constraints

Constraints:**

	- `0 <= s.length <= 5 * 10^4`

	- `s` consists of English letters, digits, symbols and spaces.

---

## Submission — 16 Jul 2026, 11:10 am (PYTHON3)

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l,r=0,0
        maxi=0
        while r<len(s):
            if s[r] in map:
                l=max(l, map[s[r]]+1)
            maxi=max(maxi,r-l+1)
            map[s[r]]=r
            r+=1

        return maxi

```
