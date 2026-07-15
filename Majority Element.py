# Moores Voting Algorithm
class Solution:
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
