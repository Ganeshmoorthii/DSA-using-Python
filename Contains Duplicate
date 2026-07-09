class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_arr=set()
        for i,v in enumerate(nums):
            if v in new_arr:
                return True
            new_arr.add(v)
        return False
