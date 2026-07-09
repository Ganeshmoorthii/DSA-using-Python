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
