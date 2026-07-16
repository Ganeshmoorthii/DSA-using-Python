# Majority Element

## Problem Description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**

## Examples

Example 1:**

```
**Input:** nums = [3,2,3]
**Output:** 3
```
**Example 2:**

```
**Input:** nums = [2,2,1,1,1,2,2]
**Output:** 2
```

**

## Constraints

Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- The input is generated such that a majority element will exist in the array.

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

---

## Submission — 16 Jul 2026, 11:13 am (PYTHON3)

```py
    def majorityElement(self, nums: List[int]) -> int:
        el=nums[0]
        cnt=1
        for i in range(1,len(nums)):
            if cnt==0:
                el=nums[i]
                cnt=1
            elif el == nums[i]:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in nums:
            if el==i:
                cnt1+=1
        if cnt1>len(nums)/2:
            return el
        return -1
class Solution:
# Moores Voting Algorithm

```
