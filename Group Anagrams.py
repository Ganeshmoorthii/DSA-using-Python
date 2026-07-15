# Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            val = "".join(sorted(word))
            if val not in map:
                map[val]=[]
            map[val].append(word)
        return list(map.values())

# Solution 2
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

---

## Submission — 15 Jul 2026, 11:18 am (PYTHON3)

### Group Anagrams

**Description:**

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

**

**Examples:**

Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

	- There is no string in strs that can be rearranged to form `"bat"`.

	- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

	- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

**

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            val = "".join(sorted(word))
            if val not in map:
                map[val]=[]
            map[val].append(word)
        return list(map.values())
```
