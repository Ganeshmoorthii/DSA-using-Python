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
