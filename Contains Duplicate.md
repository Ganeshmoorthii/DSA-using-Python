# Contains Duplicate

## Problem Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**

## Examples

Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

**

## Constraints

Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

---

## Submission — 16 Jul 2026, 11:26 am (PYTHON3)

```py
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_arr=set()
        for i,v in enumerate(nums):
            if v in new_arr:
                return True
            new_arr.add(v)
        return False

```
