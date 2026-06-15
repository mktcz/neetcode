class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = {}
        result = []
        for s in strs:
            s_sorted = "".join(sorted(s))
            if smap.get(s_sorted) is not None:
                smap[s_sorted] += [s]
            else:
                smap[s_sorted] = [s]

        return list(smap.values())
