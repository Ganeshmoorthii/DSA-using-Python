class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for i in nums:
            xor = xor^i
        return xor

---

## Submission — 15 Jul 2026, 11:07 am (PYTHON3)

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for i in nums:
            xor = xor^i
        return xor
```
